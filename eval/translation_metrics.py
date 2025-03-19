from typing import Union, Any

import evaluate
import sacrebleu
import torch
from comet import download_model, load_from_checkpoint
from evaluate import load


# loading the models
BLEURT = load("bleurt", module_type="metric", checkpoint="BLEURT-20")
MODEL_PATH = download_model("Unbabel/wmt22-comet-da")
# Load the model checkpoint:
COMET_MODEL = load_from_checkpoint(MODEL_PATH)

# Load the TER metric
TER = evaluate.load("ter")

# Compute BLEU score
def calc_dbleu_score(hypothesis: str, reference: str)-> Union[float, None]:
    """
    Calculate the BLEU score for a given hypothesis and reference text using sacrebleu.

    Parameters:
    hypothesis (str): The hypothesis text (machine translated text).
    reference (str): The reference text (actual translated text).

    Returns:
    float: The BLEU score if calculation is successful.
    "None" if an exception occurs during calculation.

    Example:
    >>> calc_dbleu_score("This is a test hypothesis.", "This is a test reference.")
    45.67
    """
    try:
        bleu = sacrebleu.corpus_bleu([hypothesis], [[reference]])
        return bleu.score
    except Exception as e:
        return None


def calc_bleurt_score(hypothesis: str, references: str) -> Union[float, None]:
    """
    Calculate the BLEURT score for given predictions and reference texts.

    Parameters:
    predictions (str): The predicted text (machine translated text).
    references (str): The reference text (actual translated text).

    Returns:
    float: The BLEURT score if calculation is successful.
    "None" if an exception occurs during calculation.

    """
    try:
        results = BLEURT.compute(predictions=[hypothesis], references=[references])
        return results['scores'][0]
    except Exception as e:
        return None


def calc_comet_score(src: str,
                     mt: str,
                     ref: str
                     ) -> Union[float, None]:
    """
    Calculate the COMET score for given source, machine translation, and reference texts.

    Parameters:
    src (str): The source text.
    mt (str): The machine-translated text.
    ref (str): The reference (actual translated) text.

    Returns:
    float: The COMET system score.

    """
    try:
        data = [
            {
                "src": src,
                "mt": mt,
                "ref": ref
            },
        ]
        # For Apple devices with Apple Silicon,
        if torch.backends.mps.is_available():
            gpu_count = 1
        else:
            gpu_count = torch.cuda.device_count()
        # if gpu_count < 0, pytorch will decide on the num_workers
        num_workers = None if gpu_count > 0 else 1
        # Call predict method:
        model_output = COMET_MODEL.predict(data, batch_size=16, gpus=gpu_count, num_workers=num_workers)
        return model_output['system_score']
    except Exception as e:
        return None


def calc_ter_score(hypothesis: str, reference: str) -> tuple[None, None] | tuple[Any, float | int | Any]:
    """
    Calculate the TER score for a given hypothesis and reference text.

    Parameters:
    hypothesis (str): The hypothesis text (machine translated text).
    reference (str): The reference text (actual translated text).

    Returns:
     int: The TER score and the number of edits if calculation is successful.
     (None, None) if an exception occurs during calculation.


    """
    try:
        results = TER.compute(predictions=[hypothesis], references=[[reference]])
        num_edits = results['num_edits']
        ter_score = (num_edits / len(reference)) * 100
        # Call predict method:
        return num_edits, ter_score
    except Exception as e:
        return  None, None