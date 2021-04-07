import PretrainedEmbeddings
import masked_cross_entropy
import Vocab
import evaluate
import trainer
import ControllableDataset
import ControllableModel
import AttentionDecoder
import ScoreModelDataset
#import modules.evaluator_polarity


# For flake8 compatibility
__all__ = [masked_cross_entropy, PretrainedEmbeddings,  Vocab,
           evaluate, trainer, ControllableDataset,ControllableModel,
           AttentionDecoder,ScoreModelDataset]
