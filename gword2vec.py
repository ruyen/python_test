import gensim, logging
import os


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()



'''
def set_input
dir_name = 트레이닝 데이터 패스
model_name = word2vec 학습 모델 이름
v_size = vector 크기
v_window = 학습 창 크기
v_min_count = 아마 word frequency의 최소 값인듯 .. 문서가 많으면 값이 좀 높아야 하고 아니면 적어야하고 ..
'''
def set_input(dir_name, model_name, v_size, v_window, v_min_count, v_workers):
    sentences = MySentences(dir_name)  # a memory-friendly iterator
    model = gensim.models.Word2Vec(sentences, size=v_size, window=v_window, min_count=v_min_count, workers=v_workers)
    model.save(model_name)
    #model = Word2Vec.load(model_name)  # you can continue training with the loaded model!
    return model


