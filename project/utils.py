import json
import numpy as np
import pickle
import config

class PriceDetection():

    def __init__(self,CRIM, ZN,INDUS,CHAS,NOX,RM, AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
        self.CRIM=CRIM
        self.ZN=ZN
        self.INDUS=INDUS
        self.CHAS=CHAS
        self.NOX=NOX
        self.RM=RM
        self.AGE=AGE
        self.DIS=DIS
        self.RAD=RAD
        self.TAX=TAX
        self.PTRATIO=PTRATIO
        self.B=B
        self.LSTAT=LSTAT

    def load_data(self):

        with open(config.model_file,"rb") as f:
            self.model = pickle.load(f)

        with open(config.scaling_file,"rb") as f:
            self.scaling = pickle.load(f)

        with open(config.data_file,"r") as f:
            self.json_data = json.load(f)



    def price_pred(self):
        self.load_data()

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.CRIM
        test_array[1] = self.ZN
        test_array[2] = self.INDUS
        test_array[3] = self.CHAS
        test_array[4] = self.NOX
        test_array[5] = self.RM
        test_array[6] = self.AGE
        test_array[7] = self.DIS
        test_array[8] = self.RAD
        test_array[9] = self.TAX
        test_array[10] = self.PTRATIO
        test_array[11] = self.B
        test_array[12] = self.LSTAT

        scaled_test_array = self.scaling.transform([test_array])

        predicted_value = self.model.predict(scaled_test_array)[0]
        return predicted_value



if __name__ == "__main__":

    CRIM  =   0.05724
    ZN    =  0.00000
    INDUS =  4.24000
    CHAS  =  0.00000
    NOX   =  0.46000
    RM    =  6.33300
    AGE   = 15.20000
    DIS   =  7.21460
    RAD   =  2.00000
    TAX   = 450.00000
    PTRATIO  = 17.90000
    B        =370.21000
    LSTAT    =  8.34000


    obj = PriceDetection(CRIM, ZN,INDUS,CHAS,NOX,RM, AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    obj.price_pred()
    
    
