import argparse

from utils.logger import Logger

def main(work_type_args):

    if work_type_args.type == 'classification_TU':

        from parsers.classification_TU import Parser
        from trainers.trainer_classification_TU import Trainer

        args = Parser().parse()
        trainer = Trainer(args)
        trainer.train()

    else:

        raise ValueError("Work Type Name <{}> is Unknown".format(work_type_args.type))


    pass

if __name__ == '__main__':

    work_type_parser = argparse.ArgumentParser()
    work_type_parser.add_argument('--type', type=str, required=True)

    main(work_type_parser.parse_args())