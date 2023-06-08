
image_similarity_html_template = """
<h1 style="margin-bottom: 5px;">圖像比對結果: {result_msg}</h1>
<h2 style="margin-bottom: 5px;">相似度: {similarity}</h2>
<table style="margin-top: 5px;">
<thead>
<tr>
<th>驗證圖片</th>
<th>本次截圖</th>
<th>差異部分</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src='./G{game_id}_ground_truth.png' width="300"></td>
<td><img src='./G{game_id}_screenshot.png' width="300"></td>
<td><img src='./G{game_id}_difference.png' width="300"></td>
</tr>
</tbody>
</table>
"""
