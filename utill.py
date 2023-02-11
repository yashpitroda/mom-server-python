    
from sumy.summarizers.lsa import LsaSummarizer
import pandas as pd
import numpy as np
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
data = "Meetings usually start when the group chair will formally announce that the meeting has started. Once the meeting has started, the first thing to accomplish is to do a roll call. Call out the names (from your list) of those who will participate in the meeting. Mark their names if they’re absent or present. If you have a copy of the past meeting summary with you, indicate the points that have been written down to remind the group of what topics they need to discuss that they were unable to do during the last one.Once the agenda has been discussed, dedicate your 100% attention to the points that the participants said. Avoid any distractions. Even if you used a cassette recorder to record the meeting’s proceedings, it’s important to listen carefully to the meeting to avoid any confusion once you’ve listened to the recording later. There might be instances that the recordings will get lost or the sound is garbled, so don’t just solely rely on the recorder. Tape recorders are there to serve you as a back-up.Aside from just listening, your role as making the meeting summary is to take down notes. Of course, you don’t necessarily need to list down everything that happened in the meeting (such as someone had a coughing fit or someone spilled their coffee on their clothes), but as mentioned above, list down the important key points that have been discussed."
class Utills:
    def lsa_method(text):
        print(text)
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer_lsa = LsaSummarizer()
        summary_2 = summarizer_lsa(parser.document, 2)
        dp = []
        final_sentence=""
        for i in summary_2:
            lp = str(i)
            dp.append(lp)
            final_sentence = ' '.join(dp)
        return final_sentence
        # lsa_method(data)