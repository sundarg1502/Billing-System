# from django.test import TestCase
import inflect

def rupess(amount):
    cvt = inflect.engine()
    blk =  int(int(amount)%100000)
    print(str(amount)[0])
    lk = f"{cvt.number_to_words(str(amount)[0])} lakh" if amount//100000 >0 else 0
    rupees = f"{cvt.number_to_words(blk)} Rupees "
    paise = int(str(amount).split(".")[-1]) if len(str(amount).split("."))>=2 else -1
    if paise>0:
        return f"{lk if lk!=0 else ""} {rupees}and {cvt.number_to_words(paise)} Paise only "
    else:
        return  f"{lk if lk!=0 else ""}{rupees}Only"

print(rupess(105201.72))