import torch
import torch.nn as nn
import os
import argparse
from bot.model import predict_model_factory
from bot.dataset import field_factory, metadata_factory
from bot.serialization import load_object
from bot.constants import MODEL_START_FORMAT

model_path = '/home/ubuntu/chatbot/pretrained-models/amazon'
epoch = 10

def main():
    torch.set_grad_enabled(False)
    print('Args loaded')
    model_args = load_object(model_path + os.path.sep + 'args')
    print('Model args loaded.')
    vocab = load_object(model_path + os.path.sep + 'vocab')
    print('Vocab loaded.')

    torch.set_default_tensor_type(torch.FloatTensor)
    print("Using CPU for inference")

    field = field_factory(model_args)
    field.vocab = vocab
    metadata = metadata_factory(model_args, vocab)

    final_path = None

    name_start = MODEL_START_FORMAT % epoch
    for path in os.listdir(model_path + os.path.sep):
        if path.startswith(name_start):
            final_path = model_path + os.path.sep + path
    if not final_path:
        raise ValueError("Model from epoch %d doesn't exist in %s" % (epoch, dir_path))


    model = predict_model_factory(model_args, metadata, final_path, field)
    print('model loaded')
    model.eval()

    question = ''
    print('\n\nBot: Hi, how can I help you?', flush=True)
    while question != 'bye':
        while True:
            print('Me: ', end='')
            question = input()
            if question:
                break

        response = model([question], sampling_strategy='greedy', max_seq_len=100)[0]
        print('Bot: ' + response)


if __name__ == '__main__':
    main()