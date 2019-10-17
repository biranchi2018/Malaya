from .. import home

MALAY_TEXT = home + '/dictionary/malay-text.txt'
MALAY_TEXT_200K = home + '/dictionary-200k/malay-text.txt'

PATH_NGRAM = {
    1: {
        'model': home + '/preprocessing/ngram1/bm_1grams.json',
        'version': 'v28',
    },
    2: {
        'model': home + '/preprocessing/ngram2/bm_2grams.json',
        'version': 'v23',
    },
    'symspell': {
        'model': home + '/preprocessing/symspell/bm_1grams.txt',
        'version': 'v28',
    },
}

S3_PATH_NGRAM = {
    1: {'model': 'v27/preprocessing/bm_1grams.json'},
    2: {'model': 'v23/preprocessing/bm_2grams.json'},
    'symspell': {'model': 'v27/preprocessing/bm_1grams.txt'},
}

PATH_PREPROCESSING = {
    1: {
        'model': home + '/preprocessing/count1/1counts_1grams.json',
        'version': 'v23',
    },
    2: {
        'model': home + '/preprocessing/count2/counts_2grams.json',
        'version': 'v23',
    },
    'english-malay': {
        'model': home + '/preprocessing/english-malay/english-malay-200k.json',
        'version': 'v23',
    },
}

S3_PATH_PREPROCESSING = {
    1: {'model': 'v23/preprocessing/counts_1grams.json'},
    2: {'model': 'v23/preprocessing/counts_2grams.json'},
    'english-malay': {'model': 'v23/preprocessing/english-malay-200k.json'},
}

PATH_STEM = {
    'lstm': {
        'model': home + '/stem/lstm/lstm-stem.pb',
        'setting': home + '/stem/lstm/lstm-stem.json',
        'version': 'v15',
    },
    'bahdanau': {
        'model': home + '/stem/bahdanau/bahdanau-stem.pb',
        'setting': home + '/stem/bahdanau/bahdanau-stem.json',
        'version': 'v15',
    },
    'luong': {
        'model': home + '/stem/luong/luong-stem.pb',
        'setting': home + '/stem/luong/luong-stem.json',
        'version': 'v15',
    },
}

S3_PATH_STEM = {
    'lstm': {
        'model': 'v15/stem/lstm-stem.pb',
        'setting': 'v15/stem/lstm-stem.json',
    },
    'bahdanau': {
        'model': 'v15/stem/bahdanau-stem.pb',
        'setting': 'v15/stem/bahdanau-stem.json',
    },
    'luong': {
        'model': 'v15/stem/luong-stem.pb',
        'setting': 'v15/stem/luong-stem.json',
    },
}

PATH_SUMMARIZE = {
    'news': {
        'model': home + '/summarize/summary-news.pb',
        'setting': home + '/summarize/summary-news.json',
        'version': 'v13',
    },
    'wiki': {
        'model': home + '/summarize/summary-wiki.pb',
        'setting': home + '/summarize/summary-wiki.json',
        'version': 'v13',
    },
}

S3_PATH_SUMMARIZE = {
    'news': {
        'model': 'v13/summarize/summary-news.pb',
        'setting': 'v13/summarize/summary-news.json',
    },
    'wiki': {
        'model': 'v13/summarize/summary-wiki.pb',
        'setting': 'v13/summarize/summary-wiki.json',
    },
}

PATH_TOXIC = {
    'multinomial': {
        'model': home + '/toxic/multinomial/multinomials-toxic.pkl',
        'vector': home + '/toxic/multinomial/vectorizer-toxic.pkl',
        'version': 'v30',
    },
    'bert': {
        'base': {
            'model': home + '/toxic/base/bert-toxic.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'version': 'v30',
        },
        'small': {
            'model': home + '/toxic/small/bert-toxic.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'version': 'v30',
        },
    },
}

S3_PATH_TOXIC = {
    'multinomial': {
        'model': 'v30/multinomials-toxic.pkl',
        'vector': 'v30/vectorizer-toxic.pkl',
    },
    'bert': {
        'base': {
            'model': 'v27/toxicity/bert-base-toxicity.pb',
            'vocab': 'v27/sp10m.cased.v4.vocab',
            'tokenizer': 'v27/sp10m.cased.v4.model',
        },
        'small': {
            'model': 'v27/toxicity/bert-small-toxicity.pb',
            'vocab': 'v27/sp10m.cased.v4.vocab',
            'tokenizer': 'v27/sp10m.cased.v4.model',
        },
    },
}

PATH_POS = {
    'bert': {
        'base': {
            'model': home + '/pos/bert/base/bert-pos.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'setting': home + '/pos/dictionary-pos.json',
            'version': 'v30',
        },
        'small': {
            'model': home + '/pos/bert/small/bert-pos.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'setting': home + '/pos/dictionary-pos.json',
            'version': 'v30',
        },
    },
    'xlnet': {
        'base': {
            'model': home + '/pos/xlnet/base/xlnet-pos.pb',
            'vocab': home + '/xlnet/sp10m.cased.v5.vocab',
            'tokenizer': home + '/xlnet/sp10m.cased.v5.model',
            'setting': home + '/pos/dictionary-pos.json',
            'version': 'v30',
        }
    },
    'albert': {
        'base': {
            'model': home + '/pos/albert/base/xlnet-pos.pb',
            'vocab': home + '/albert/sp10m.cased.v6.vocab',
            'tokenizer': home + '/albert/sp10m.cased.v6.model',
            'setting': home + '/pos/dictionary-pos.json',
            'version': 'v30',
        }
    },
}

S3_PATH_POS = {
    'bert': {
        'base': {
            'model': 'v30/pos/bert-base-pos.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
            'setting': 'bert-bahasa/dictionary-pos.json',
        },
        'small': {
            'model': 'v30/pos/bert-small-pos.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
            'setting': 'bert-bahasa/dictionary-pos.json',
        },
    },
    'xlnet': {
        'base': {
            'model': 'v30/pos/xlnet-base-pos.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v5.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v5.model',
            'setting': 'bert-bahasa/dictionary-pos.json',
        }
    },
    'albert': {
        'base': {
            'model': 'v30/pos/albert-base-pos.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v6.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v6.model',
            'setting': 'bert-bahasa/dictionary-pos.json',
        }
    },
}


PATH_LANG_DETECTION = {
    'multinomial': {
        'model': home
        + '/language-detection/multinomial/multinomial-language-detection.pkl',
        'vector': home
        + '/language-detection/multinomial/vectorizer-language-detection.pkl',
        'version': 'v10.2',
    },
    'sgd': {
        'model': home + '/language-detection/sgd/sgd-language-detection.pkl',
        'vector': home
        + '/language-detection/multinomial/vectorizer-language-detection.pkl',
        'version': 'v10.2',
    },
    'deep': {
        'model': home
        + '/language-detection/deep/model.ckpt.data-00000-of-00001',
        'index': home + '/language-detection/deep/model.ckpt.index',
        'meta': home + '/language-detection/deep/model.ckpt.meta',
        'vector': home
        + '/language-detection/multinomial/vectorizer-language-detection.pkl',
        'version': 'v10.2',
    },
}

S3_PATH_LANG_DETECTION = {
    'multinomial': {
        'model': 'v10/language-detection/multinomial-language-detection.pkl',
        'vector': 'v10/language-detection/language-detection-vectorizer.pkl',
    },
    'sgd': {
        'model': 'v10/language-detection/sgd-language-detection.pkl',
        'vector': 'v10/language-detection/language-detection-vectorizer.pkl',
    },
    'deep': {
        'model': 'v10/language-detection/model.ckpt.data-00000-of-00001',
        'index': 'v10/language-detection/model.ckpt.index',
        'meta': 'v10/language-detection/model.ckpt.meta',
        'vector': 'v10/language-detection/language-detection-vectorizer.pkl',
    },
}

PATH_ENTITIES = {
    'bert': {
        'base': {
            'model': home + '/entity/bert/base/bert-entity.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'setting': home + '/entity/dictionary-entities.json',
            'version': 'v30',
        },
        'small': {
            'model': home + '/entity/bert/small/bert-entity.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'setting': home + '/entity/dictionary-entities.json',
            'version': 'v30',
        },
    },
    'xlnet': {
        'base': {
            'model': home + '/entity/xlnet/base/xlnet-entity.pb',
            'vocab': home + '/xlnet/sp10m.cased.v5.vocab',
            'tokenizer': home + '/xlnet/sp10m.cased.v5.model',
            'setting': home + '/entity/dictionary-entities.json',
            'version': 'v30',
        }
    },
    'albert': {
        'base': {
            'model': home + '/entity/albert/base/xlnet-entity.pb',
            'vocab': home + '/albert/sp10m.cased.v6.vocab',
            'tokenizer': home + '/albert/sp10m.cased.v6.model',
            'setting': home + '/entity/dictionary-entities.json',
            'version': 'v30',
        }
    },
}

S3_PATH_ENTITIES = {
    'bert': {
        'base': {
            'model': 'v30/entity/bert-base-entity.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
            'setting': 'bert-bahasa/dictionary-entities.json',
        },
        'small': {
            'model': 'v30/entity/bert-small-entity.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
            'setting': 'bert-bahasa/dictionary-entities.json',
        },
    },
    'xlnet': {
        'base': {
            'model': 'v30/entity/xlnet-base-entity.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v5.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v5.model',
            'setting': 'bert-bahasa/dictionary-entities.json',
        }
    },
    'albert': {
        'base': {
            'model': 'v30/entity/albert-base-entity.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v6.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v6.model',
            'setting': 'bert-bahasa/dictionary-entities.json',
        }
    },
}

PATH_SENTIMENT = {
    'multinomial': {
        'model': home + '/sentiment/multinomial/multinomial-sentiment.pkl',
        'vector': home
        + '/sentiment/multinomial/multinomial-sentiment-tfidf.pkl',
        'version': 'v30',
    },
    'bert': {
        'base': {
            'model': home + '/sentiment/bert/base/bert-sentiment.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'version': 'v30',
        },
        'small': {
            'model': home + '/sentiment/bert/small/bert-sentiment.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'version': 'v30',
        },
    },
    'albert': {
        'base': {
            'model': home + '/sentiment/albert/base/albert-sentiment.pb',
            'vocab': home + '/albert/sp10m.cased.v6.vocab',
            'tokenizer': home + '/albert/sp10m.cased.v6.model',
            'version': 'v30',
        }
    },
    'xlnet': {
        'base': {
            'model': home + '/sentiment/xlnet/base/albert-sentiment.pb',
            'vocab': home + '/xlnet/sp10m.cased.v5.vocab',
            'tokenizer': home + '/xlnet/sp10m.cased.v5.model',
            'version': 'v30',
        }
    },
}

S3_PATH_SENTIMENT = {
    'multinomial': {
        'model': 'v30/sentiment/multinomial-sentiment.pkl',
        'vector': 'v30/sentiment/multinomial-sentiment-tfidf.pkl',
    },
    'bert': {
        'base': {
            'model': 'v30/sentiment/bert-base-sentiment.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
        },
        'small': {
            'model': 'v30/sentiment/bert-small-sentiment.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
        },
    },
    'albert': {
        'base': {
            'model': 'v30/sentiment/albert-base-sentiment.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v6.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v6.model',
        }
    },
    'xlnet': {
        'base': {
            'model': 'v30/sentiment/xlnet-base-sentiment.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v5.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v5.model',
        }
    },
}

PATH_SUBJECTIVE = {
    'bahdanau': {
        'model': home + '/subjective/bahdanau/bahdanau-subjective.pb',
        'setting': home + '/subjective/subjective-dictionary.json',
        'version': 'v24',
    },
    'luong': {
        'model': home + '/subjective/luong/luong-subjective.pb',
        'setting': home + '/subjective/subjective-dictionary.json',
        'version': 'v24',
    },
    'self-attention': {
        'model': home + '/subjective/luong/luong-subjective.pb',
        'setting': home + '/subjective/subjective-dictionary.json',
        'version': 'v24',
    },
    'multinomial': {
        'model': home + '/subjective/multinomial/multinomial-subjective.pkl',
        'vector': home
        + '/subjective/multinomial/multinomial-subjective-tfidf.pkl',
        'version': 'v10',
    },
    'xgb': {
        'model': home + '/subjective/xgb/xgboost-subjective.pkl',
        'vector': home + '/subjective/xgb/xgboost-subjective-tfidf.pkl',
        'version': 'v10',
    },
    'multilanguage': {
        'model': home
        + '/subjective/multilanguage/bert-multilanguage-subjective.pb',
        'vocab': home + '/bert/multilanguage-vocab.txt',
        'version': 'v27',
    },
    'base': {
        'model': home + '/subjective/base/bert-subjective.pb',
        'vocab': home + '/bert/sp10m.cased.v4.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v4.model',
        'version': 'v27',
    },
    'small': {
        'model': home + '/subjective/small/bert-subjective.pb',
        'vocab': home + '/bert/sp10m.cased.v4.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v4.model',
        'version': 'v27',
    },
}

S3_PATH_SUBJECTIVE = {
    'bahdanau': {
        'model': 'v24/subjective/bahdanau-subjective.pb',
        'setting': 'v24/subjective/subjective-dictionary.json',
    },
    'luong': {
        'model': 'v24/subjective/luong-subjective.pb',
        'setting': 'v24/subjective/subjective-dictionary.json',
    },
    'self-attention': {
        'model': 'v24/subjective/self-attention-subjective.pb',
        'setting': 'v24/subjective/subjective-dictionary.json',
    },
    'multinomial': {
        'model': 'v10/subjective/multinomial-subjective.pkl',
        'vector': 'v10/subjective/multinomial-subjective-tfidf.pkl',
    },
    'xgb': {
        'model': 'v10/subjective/xgboost-subjective.pkl',
        'vector': 'v10/subjective/xgboost-subjective-tfidf.pkl',
    },
    'multilanguage': {
        'model': 'v27/subjective/bert-multilanguage-subjective.pb',
        'vocab': 'v24/multilanguage-vocab.txt',
    },
    'base': {
        'model': 'v27/subjective/bert-base-subjective.pb',
        'vocab': 'v27/sp10m.cased.v4.vocab',
        'tokenizer': 'v27/sp10m.cased.v4.model',
    },
    'small': {
        'model': 'v27/subjective/bert-small-subjective.pb',
        'vocab': 'v27/sp10m.cased.v4.vocab',
        'tokenizer': 'v27/sp10m.cased.v4.model',
    },
}

PATH_EMOTION = {
    'multinomial': {
        'model': home + '/emotion/multinomial/multinomial-emotion.pkl',
        'vector': home + '/emotion/multinomial/multinomial-emotion-tfidf.pkl',
        'version': 'v30',
    },
    'bert': {
        'base': {
            'model': home + '/emotion/bert/base/bert-emotion.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'version': 'v30',
        },
        'small': {
            'model': home + '/emotion/bert/small/bert-emotion.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'version': 'v30',
        },
    },
    'albert': {
        'base': {
            'model': home + '/emotion/albert/base/albert-emotion.pb',
            'vocab': home + '/albert/sp10m.cased.v6.vocab',
            'tokenizer': home + '/albert/sp10m.cased.v6.model',
            'version': 'v30',
        }
    },
    'xlnet': {
        'base': {
            'model': home + '/emotion/xlnet/base/albert-emotion.pb',
            'vocab': home + '/xlnet/sp10m.cased.v5.vocab',
            'tokenizer': home + '/xlnet/sp10m.cased.v5.model',
            'version': 'v30',
        }
    },
}

S3_PATH_EMOTION = {
    'multinomial': {
        'model': 'v30/emotion/multinomial-emotion.pkl',
        'vector': 'v30/emotion/multinomial-emotion-tfidf.pkl',
    },
    'bert': {
        'base': {
            'model': 'v30/emotion/bert-base-emotion.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
        },
        'small': {
            'model': 'v30/emotion/bert-small-emotion.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
        },
    },
    'albert': {
        'base': {
            'model': 'v30/emotion/albert-base-emotion.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v6.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v6.model',
        }
    },
    'xlnet': {
        'base': {
            'model': 'v30/emotion/xlnet-base-emotion.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v5.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v5.model',
        }
    },
}

PATH_DEPEND = {
    'bert': {
        'base': {
            'model': home + '/dependency/bert/base/bert-dependency.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'version': 'v30',
        }
    },
    'albert': {
        'base': {
            'model': home + '/dependency/albert/base/albert-dependency.pb',
            'vocab': home + '/albert/sp10m.cased.v6.vocab',
            'tokenizer': home + '/albert/sp10m.cased.v6.model',
            'version': 'v30',
        }
    },
    'xlnet': {
        'base': {
            'model': home + '/dependency/xlnet/base/xlnet-dependency.pb',
            'vocab': home + '/xlnet/sp10m.cased.v5.vocab',
            'tokenizer': home + '/xlnet/sp10m.cased.v5.model',
            'version': 'v30',
        }
    },
}

S3_PATH_DEPEND = {
    'bert': {
        'base': {
            'model': 'v30/dependency/bert-base-dependency.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
        }
    },
    'albert': {
        'base': {
            'model': 'v30/dependency/albert-base-dependency.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v6.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v6.model',
        }
    },
    'xlnet': {
        'base': {
            'model': 'v30/dependency/xlnet-base-dependency.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v5.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v5.model',
        }
    },
}

PATH_RELEVANCY = {
    'bert': {
        'base': {
            'model': home + '/relevancy/bert/base/bert-relevancy.pb',
            'vocab': home + '/bert/sp10m.cased.v4.vocab',
            'tokenizer': home + '/bert/sp10m.cased.v4.model',
            'version': 'v30',
        }
    },
    'albert': {
        'base': {
            'model': home + '/relevancy/albert/base/albert-relevancy.pb',
            'vocab': home + '/albert/sp10m.cased.v6.vocab',
            'tokenizer': home + '/albert/sp10m.cased.v6.model',
            'version': 'v30',
        }
    },
    'xlnet': {
        'base': {
            'model': home + '/relevancy/xlnet/base/albert-relevancy.pb',
            'vocab': home + '/xlnet/sp10m.cased.v5.vocab',
            'tokenizer': home + '/xlnet/sp10m.cased.v5.model',
            'version': 'v30',
        }
    },
}
S3_PATH_RELEVANCY = {
    'bert': {
        'base': {
            'model': 'v30/relevancy/bert-base-relevancy.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v4.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v4.model',
        }
    },
    'albert': {
        'base': {
            'model': 'v30/relevancy/albert-base-relevancy.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v6.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v6.model',
        }
    },
    'xlnet': {
        'base': {
            'model': 'v30/relevancy/xlnet-base-relevancy.pb',
            'vocab': 'bert-bahasa/sp10m.cased.v5.vocab',
            'tokenizer': 'bert-bahasa/sp10m.cased.v5.model',
        }
    },
}

PATH_SIMILARITY = {
    'multilanguage': {
        'model': home + '/similarity/multilanguage/bert.pb',
        'vocab': home + '/bert/multilanguage-vocab.txt',
        'version': 'v24',
    },
    'base': {
        'model': home + '/base/base/bert.pb',
        'vocab': home + '/bert/sp10m.cased.v4.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v4.model',
        'version': 'v27',
    },
    'small': {
        'model': home + '/small/small/bert.pb',
        'vocab': home + '/bert/sp10m.cased.v4.vocab',
        'tokenizer': home + '/bert/sp10m.cased.v4.model',
        'version': 'v27',
    },
}

S3_PATH_SIMILARITY = {
    'multilanguage': {
        'model': 'v26/similarity/bert-similarity.pb',
        'vocab': 'v24/multilanguage-vocab.txt',
    },
    'base': {
        'model': 'v27/similarity/bert-base-similarity.pb',
        'vocab': 'v27/sp10m.cased.v4.vocab',
        'tokenizer': 'v27/sp10m.cased.v4.model',
    },
    'small': {
        'model': 'v27/similarity/bert-small-similarity.pb',
        'vocab': 'v27/sp10m.cased.v4.vocab',
        'tokenizer': 'v27/sp10m.cased.v4.model',
    },
}

PATH_BERT = {
    'base': {
        'path': home + '/bert-model/base',
        'directory': home + '/bert-model/base/bert-base/',
        'model': {
            'model': home + '/bert-model/base/bert-bahasa-base.tar.gz',
            'version': 'v30',
        },
    },
    'small': {
        'path': home + '/bert-model/small',
        'directory': home + '/bert-model/small/bert-small/',
        'model': {
            'model': home + '/bert-model/small/bert-bahasa-small.tar.gz',
            'version': 'v30',
        },
    },
}

S3_PATH_BERT = {
    'base': {'model': 'bert-bahasa/bert-base-13-9-2019.tar.gz'},
    'small': {'model': 'bert-bahasa/bert-small-19-9-2019.tar.gz'},
}

PATH_XLNET = {
    'base': {
        'path': home + '/xlnet-model/base',
        'directory': home + '/xlnet-model/base/xlnet-base/',
        'model': {
            'model': home + '/xlnet-model/base/xlnet-base.tar.gz',
            'version': 'v30',
        },
    }
}

S3_PATH_XLNET = {'base': {'model': 'bert-bahasa/xlnet-base-30-9-2019.tar.gz'}}

PATH_ALBERT = {
    'base': {
        'path': home + '/albert-model/base',
        'directory': home + '/albert-model/base/albert-base/',
        'model': {
            'model': home + '/albert-model/base/albert-base.tar.gz',
            'version': 'v30',
        },
    }
}

S3_PATH_ALBERT = {
    'base': {'model': 'bert-bahasa/albert-base-11-10-2019.tar.gz'}
}
