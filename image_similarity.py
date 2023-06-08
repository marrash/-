from enum import Enum
from typing import Tuple

# Third-Party Library Modules
import cv2 as cv
import numpy as np


class Algorithm(Enum):
    P_HASH = 1
    SIFT = 2


def calculate_image_similarity(algorithm: Algorithm, img1_path: str, img2_path: str, height_range: tuple = None) -> Tuple[float, cv.Mat]:
    """
    計算兩張圖片之間的相似程度

    Args:
     - algorithm: 選擇使用的演算法 (請參考 Algorithm Enum)
     - img1_path: 第一張圖片的路徑
     - img2_path: 第二張圖片的路徑
     - height_range: 欲先對圖片前處理的剪裁範圍

    Returns:
     - float: 兩張圖片的相似度分數，範圍為 0.0 到 1.0
    """

    # 讀取圖片
    img1 = cv.imread(img1_path)
    img2 = cv.imread(img2_path)

    # 剪裁圖片
    if height_range is not None:
        h1, w1 = img1.shape[:2]
        img1 = img1[int(h1*height_range[0]):int(h1*height_range[1]), 0:w1-1]

        h2, w2 = img2.shape[:2]
        img2 = img2[int(h2*height_range[0]):int(h2*height_range[1]), 0:w2-1]

    similarity = 0

    # 使用指定算法
    if algorithm == Algorithm.P_HASH:
        similarity = _calculate_similarity_by_phash(img1, img2)
    elif algorithm == Algorithm.SIFT:
        similarity = _calculate_similarity_by_sift(img1, img2)

    diff_img = _get_diff_image(img1, img2)

    return similarity, diff_img


def _calculate_similarity_by_phash(img1: cv.Mat, img2: cv.Mat) -> float:
    """
    使用感知哈希算法(Perceptual Hash) 計算兩張圖片的相似度

    Args:
     - img1 (cv.Mat): OpenCV 圖片格式
     - img2 (cv.Mat): OpenCV 圖片格式

    Returns:
     - float: 兩張圖片的相似度分數，範圍為 0.0 到 1.0
    """

    phash1 = _calculate_phash(img1)
    phash2 = _calculate_phash(img2)

    # Calculate the Hamming distance between the two hashes
    distance = np.count_nonzero(phash1 != phash2)

    # Normalize the distance to the range [0, 1]
    return 1 - distance / 64.0


def _calculate_phash(image: cv.Mat):
    """
    計算指定圖片的 perceptual hash 數值

    Args:
     - image (cv.Mat): OpenCV 圖片格式

    Returns:
     - np.ndarray: 8x8 的 numpy 陣列, 內含布林值, 表示每個離散餘弦變換 (DCT) 係數是否大於平均值
    """
    
    # 將圖片大小調整為 32x32
    resized = cv.resize(image, (32, 32), interpolation = cv.INTER_AREA)
    
    # 將圖片轉換為灰階圖
    gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
    
    # 計算灰階圖的離散餘弦變換 (Discrete Cosine Transform, DCT)
    dct = cv.dct(np.float32(gray))

    # 僅保留左上角的 8x8 矩陣 (這些是低頻 DCT 係數)
    dct = dct[:8, :8]
    
    # 計算 DCT 係數的平均值
    mean = np.mean(dct)
    
    # 若 DCT 係數小於平均值則替換為 0，否則替換為 1
    phash = dct > mean

    return phash


def _calculate_similarity_by_sift(img1: cv.Mat, img2: cv.Mat) -> float:
    """
    使用 SIFT 特徵計算兩張圖片的相似度

    Args:
     - img1 (cv.Mat): OpenCV 圖片格式
     - img2 (cv.Mat): OpenCV 圖片格式

    Returns:
     - float: 兩張圖片的相似度分數，範圍為 0.0 到 1.0
    """
    
    # 將兩張圖片轉換為灰階圖
    img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

    # 利用 SIFT 方法計算兩張灰度圖的特徵點和特徵描述符
    sift = cv.SIFT_create()
    keypoint1, descriptor1 = sift.detectAndCompute(img1_gray, None)
    keypoint2, descriptor2 = sift.detectAndCompute(img2_gray, None)

    # 使用 FLANN 匹配器進行特徵匹配
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptor1, descriptor2, k=2)

    # 初始化匹配點標記列表，用於後續的 Lowe's 比例測試
    matches_mask = [[0, 0] for _ in range(len(matches))]
    
    # 應用 Lowe's 比例測試（Ratio Test）找出好的匹配點
    good_matches = []
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            good_matches.append(m)
            matches_mask[i] = [1, 0] # 標記為好的匹配點

    # 取得好的匹配點的關鍵點座標
    img1_pts = np.float32([keypoint1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    img2_pts = np.float32([keypoint2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # 利用 RANSAC 方法計算從 img1_pts 到 img2_pts 的單應性轉換矩陣 M
    M, mask = cv.findHomography(img1_pts, img2_pts, cv.RANSAC, 5.0)
    matches_mask = mask.ravel().tolist()

    # 繪製匹配點並顯示 (如果需要的話)
    draw_params = dict(
        matchColor = (0, 255, 0), # 繪製匹配點的顏色為綠色
        singlePointColor = None,
        matchesMask = matches_mask, # 僅繪製被標記為好的匹配點
        flags = 2
    )
    # matched_result = cv.drawMatches(img1, keypoint1, img2, keypoint2, good_matches, None, **draw_params)
    # cv.imshow("Matched Features", matched_result)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # 基於好的匹配點數量與總匹配點數量計算特徵匹配分數
    feature_matching_score = len(good_matches) / len(matches)

    # 計算兩張圖片的直方圖並進行歸一化處理
    hist1 = cv.calcHist([img1], [0], None, [256], [0,256])
    hist2 = cv.calcHist([img2], [0], None, [256], [0,256])
    cv.normalize(hist1, hist1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
    cv.normalize(hist2, hist2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

    # 利用直方圖的相關性（Correlation）來計算相似度分數
    histogram_score = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)

    # 將特徵匹配分數和直方圖相似度分數進行加權平均，得到最終的相似度分數
    final_score = 0.5*feature_matching_score + 0.5*histogram_score
    
    return final_score


def _get_diff_image(img1: cv.Mat, img2: cv.Mat) -> cv.Mat:
    """
    計算兩張圖片的差異，並將差異處標記為紅色

    Args:
     - img1 (cv.Mat): OpenCV 圖片格式
     - img2 (cv.Mat): OpenCV 圖片格式

    Returns:
     - cv.Mat: 標記出差異區域的圖片
    """

    # 取得兩張圖片的最小高度與寬度
    height = min(img1.shape[0], img2.shape[0])
    width = min(img1.shape[1], img2.shape[1])

    # 將兩張圖片縮放至相同大小
    img1 = cv.resize(img1, (width, height))
    img2 = cv.resize(img2, (width, height))

    # 計算兩張圖片的絕對差值
    difference = cv.absdiff(img1, img2)

    # 將差異圖片轉換為灰階
    difference = cv.cvtColor(difference, cv.COLOR_BGR2GRAY)

    # 對差異圖片進行二值化處理，將差異明顯的部分標記出來
    _, difference = cv.threshold(difference, 128, 255, cv.THRESH_BINARY)

    # 將二值化後的差異圖片轉換為彩色，並將差異部分設為紅色
    colored_difference = cv.cvtColor(difference, cv.COLOR_GRAY2BGR)
    colored_difference[difference == 255] = [0, 0, 255]

    # 回傳標記了差異的彩色圖片
    return colored_difference


def preview_cropped_image(image_path: str, height_range: tuple, width_range: tuple):
    """
    剪裁圖片預覽工具

    Args:
     - image_path (str): 圖片路徑
     - height_range (tuple): 圖片高度剪裁範圍
     - width_range (tuple): 圖片寬度剪裁範圍
    """

    img = cv.imread(image_path)
    h, w = img.shape[:2]
    img = img[int(h*height_range[0]):int(h*height_range[1]), int(w*width_range[0]):int(w*width_range[1])]

    cv.imshow("cropped result", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    image_path = r'./KKGAME_PIC/G11_ground_truth.png'
    preview_cropped_image(image_path, (0.31, 0.72), (0, 1))
    
    # img1_path = r'./KKGAME_REPORT/kkgame_report_20230530193822/G7_ground_truth.png'
    # img2_path = r'./KKGAME_REPORT/kkgame_report_20230530193822/G7_screenshot.png'
    # img3_path = r'./KKGAME_REPORT/kkgame_report_20230531145847/G7_screenshot.png'

    # similarity1, diff_img1 = calculate_image_similarity(Algorithm.P_HASH, img1_path, img2_path, (0.35, 0.75))
    # similarity2, diff_img2 = calculate_image_similarity(Algorithm.P_HASH, img1_path, img3_path, (0.35, 0.75))
    
    # print(similarity1, similarity2)
    
    # cv.imshow("Diff 1", diff_img1)
    # cv.imshow("Diff 2", diff_img2)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
