from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast(vocab_file="/gpfs/home/lmunad/hpc_workshop_060324/BatteryBert-DCDREU/newtokenizer/newBERTTokenizer-vocab.txt")
tokenizer.save_pretrained("/gpfs/home/lmunad/hpc_workshop_060324/BatteryBert-DCDREU/newtokenizer")
