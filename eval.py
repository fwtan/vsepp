from vocab import Vocabulary
import evaluation
evaluation.evalrank("data/runs/coco_vse++_vggfull_restval_finetune/model_best.pth.tar", data_path="data/data", split="test")