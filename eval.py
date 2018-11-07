from vocab import Vocabulary
import evaluation
evaluation.evalrank("data/runs/coco_vse++/model_best.pth.tar", data_path="data/data", split="test")