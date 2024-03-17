from get_ply import SFM
from get_obj import gen_obj

DATASET = "1"

gen_ply = SFM(f"datasets\\{DATASET}")
gen_ply()

gen_obj(DATASET)