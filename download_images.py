from simple_image_download import simple_image_download as simp


response = simp.simple_image_download

keywords = ["nike logo"]
for i in keywords:
    response().download(i,20)