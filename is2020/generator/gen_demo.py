from pathlib import Path


from is2020.templates.audio_table import table_with_texts
from is2020.templates.frame import header, footer


code_map = {
    "nsf_adv": "NSF-adv",
    "nsf_adv_tts": "Tacotron2 + NSF-adv",
    "pwg": "Parallel WaveGAN",
    "pwg_tts": "Tacotron2 + Parallel WaveGAN",
    "h_sinc_nsf": "hn-sinc-NSF",
    "h_sinc_nsf_tts": "Tacotron2 + hn-sinc-NSF",
    "nhv_noadv": "NHV-noadv",
    "original": "Original",
    "nhv": "NHV(proposed)",
    "nhv_tts": "Tacotron2 + NHV",
    "wavenet": "MoL WaveNet"
}

copy_id = list(range(9991, 9998))
tts_id = [9916, 9917, 9918, 9920, 9922, 9923, 9924]

copy_model = ["original", "nhv", "pwg", "nsf_adv", "wavenet", "h_sinc_nsf", "nhv_noadv"]
tts_model = ["original", "nhv_tts", "pwg_tts", "nsf_adv_tts", "h_sinc_nsf_tts"]

copy_text = [
    "这人#1一哆嗦#3，方向盘#1也#1把不#1稳了#3，差点#1撞上了#1高速#1边道#1护栏#4。",
    "那#1女孩儿#1委屈的#1说#3：“我#1一回头#1见你#1已经#1进去了#3我#1不敢#1进去啊#4！",
    "小明#1摇摇头说#3：不是#3，我#1只是#1美女#1看多了#3，想#1换个#1口味#1而已#4。",
    "接下来#3，红娘#1要求#1记者#1交费#3，记者#1表示#3不知#1表姐#1身份证#1号码#4。",
    "李东蓊#1表示#3，自己#1当时#1在#1法庭上#2发表了#1一次#1独特的#1公诉#1意见#4。",
    "另一#1男子#1扑了#1上来#3，手里#1拿着#1明晃晃的#1长刀#3，向他#1胸口#1直刺#4。",
    "今天#3，快递员#1拿着#1一个#1快递#1在#1办公室#1喊#3：秦王#1是#1哪个#3，有他#1快递#4？"
]

tts_text = [
    "随着#1天气#1转热#3，各地的#1游泳#1场所#1开始#1人头#1攒动#4。",
    "更让#1徐先生#1纳闷的是#3，房客的#1手机#1也#1打不#1通了#4。",
    "遇到#1颠簸时#3，应#1听从#1乘务员的#1安全#1指令#3，回座位#1坐好#4。",
    "傍晚#2七个#1小人#1回来了#3，白雪#1公主说#3：你们#1就是#1我#1命中的#1七个#1小矮人吧#4。",
    "一种#2表示#1商品#1所有权的#1财物#1证券#3，也称#1商品#1证券#3，如#1提货单#2、交货单#4。",
    "会有#1很#1丰富的#1东西#1留下来#3，说都#1说不完#4。",
    "这句话#1像#1从天#1而降#3，吓得#1四周#1一片#1寂静#4。",
]

copy_audios = []
copy_titles = []
root = Path("samples/")
for i in copy_id:
    audios = []
    titles = []
    for model_id in copy_model:
        audios.append(str(root / model_id / f"{i:06d}.wav"))
        titles.append(code_map[model_id])
    copy_audios.append(audios)
    copy_titles.append(titles)
tts_audios = []
tts_titles = []
for i in tts_id:
    audios = []
    titles = []
    for model_id in tts_model:
        audios.append(str(root / model_id / f"{i:06d}.wav"))
        titles.append(code_map[model_id])
    tts_audios.append(audios)
    tts_titles.append(titles)

if __name__ == "__main__":
    page = header("IS2020 Online Supplement") + \
        """
        <div class="page-header">
            <h1>Neural Homomorphic Vocoder <small>Online supplement for InterSpeech Submission</small></h1>
        </div>
        <h3> Authors </h3>
        <div class="row">
            <div class="col-md-4">
                <address>
                    <strong>Zhijun Liu</strong><br>
                    <a href="mailto:#">liuzj[at]pm[dot]me</a>
                </address>
            </div>
            <div class="col-md-4">
                <address>
                    <strong>Kuan Chen</strong><br>
                    <a href="mailto:#">azrealkuan[at]gmail[dot]com</a>
                </address>
            </div>
            <div class="col-md-4">
                <address>
                    <strong>Kai Yu</strong><br>
                    <a href="mailto:#">kai.yu[at]sjtu[dot]edu[dot]cn</a>
                </address>
            </div>
        </div>
        <p>
            The <a href="https://www.data-baker.com/open_source.html">CSMSC open source speech dataset</a> is used for the demo. 
        <h3> Copy Synthesis Demos </h3>
        """ + \
        table_with_texts(
            copy_text,
            copy_audios,
            copy_titles,
            width=3
        ) + \
        """<h3> Text-to-Speech Demos </h3>""" + \
        table_with_texts(
            tts_text,
            tts_audios,
            tts_titles,
            width=3
        ) + \
        footer()
    with open("is2020/index.html", "w") as f:
        f.write(page)
