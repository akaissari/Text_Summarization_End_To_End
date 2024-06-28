from TextSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_predict_config()
        if self.config.trained:
            self.tokenizer_path = self.config.tokenizer_path
            self.model_path = self.config.model_path
        else:
            self.tokenizer_path = self.config.model_ckpt
            self.model_path = self.config.model_ckpt



    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipeline_ = pipeline("summarization", model=self.model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipeline_(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)
        return output