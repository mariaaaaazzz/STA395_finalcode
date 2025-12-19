# Lightweight stub to allow `from wordcloud import WordCloud` to succeed
# If the real `wordcloud` package is installed, Python will prefer that.
import numpy as np

class WordCloud:
    def __init__(self, width=800, height=400, background_color="white", **kwargs):
        self.width = width
        self.height = height
        self.background_color = background_color
    def generate(self, text):
        # return a blank RGB image so plt.imshow works in the notebook
        return np.zeros((self.height, self.width, 3), dtype=np.uint8)
