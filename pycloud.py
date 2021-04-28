import stylecloud

stylecloud.gen_stylecloud(file_path='words.txt',
                          icon_name='fas fa-virus',
                          colors=['#184e77','#1e6091','#1a759f','#168aad','#34a0a4','#52b69a','#76c893','#99d98c','#b5e48c','#d9ed92'],
                          background_color= "black",
                          size=(1024, 800),
                          max_font_size=200,
                          max_words=500,
                          invert_mask=False,
                          )