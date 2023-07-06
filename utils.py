import pickle
import json
import numpy as np
import config
class DaimondData():
    def __init__(self,carat,cut,clarity,depth,table,x,y,z,color):
        print("**************INIT FUNCTION************")
        self.carat=carat
        self.cut=cut
        self.clarity=clarity
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.color=color
    def __load_saved_data(self):
        model_file_name=config.MODEL_FILE_PATH
        with open(model_file_name,'rb') as f:
            self.model=pickle.load(f)
        json_file_name=config.JSON_FILE_PATH
        with open(json_file_name,'r') as f:
            self.json_data=json.load(f)

    def get_predicted_price(self):
        self.__load_saved_data()
        cut=self.json_data['Cut'][self.cut]
        clarity=self.json_data['Clarity'][self.clarity]
        color="color_"+self.color

        color_index=self.json_data['Column Name'].index(color)

        test_array=np.zeros([1,self.model.n_features_in_])
        test_array[0,0]=self.carat
        test_array[0,1]=cut
        test_array[0,2]=clarity
        test_array[0,3]=self.depth
        test_array[0,4]=self.table
        test_array[0,5]=self.x
        test_array[0,6]=self.y
        test_array[0,7]=self.z
        test_array[0,color_index]=1

        predicted_price=np.around(self.model.predict(test_array)[0],3)
        return predicted_price