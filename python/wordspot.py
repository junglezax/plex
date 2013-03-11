import os
import cv2
import settings
import cPickle
import pdb
import matplotlib.pyplot as plt

from char_det import CharDetector
from word_det_old import WordDetector
from display import OutputCharBbs, DrawCharBbs
from helpers import GetCachePath

# load in test image
#img_name = 'IMG_2532_double.JPG'
img_name = 'scales.JPG'
img = cv2.imread(os.path.join('data',img_name))

cache_bbs_path = GetCachePath(img_name)
if os.path.exists(cache_bbs_path):
    print 'Found cached character bbs'
    with open(cache_bbs_path,'rb') as fid:
        char_bbs = cPickle.load(fid)
else:
    with open(settings.char_clf_name,'rb') as fid:
        rf = cPickle.load(fid)
    print 'Loaded character classifier'

    # run character detection to get bbs
    char_bbs = CharDetector(img, settings.hog, rf, settings.canon_size,
                            settings.alphabet_master, min_height=0.03,
                            detect_idxs=settings.detect_idxs,
                            debug=True, score_thr=.1)
    with open(cache_bbs_path,'wb') as fid:
        cPickle.dump(char_bbs,fid)

#OutputCharBbs(img, char_bbs, settings.alphabet_master)

# run word detection
lexicon = ['ANS']
match_bbs = WordDetector(char_bbs, lexicon, settings.alphabet_master)

for match_bb in match_bbs:
    # draw match
    DrawCharBbs(img, match_bb[0], settings.alphabet_master)
    plt.show()
