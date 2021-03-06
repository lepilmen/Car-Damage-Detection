import os


def Prediction (modelType,img_path) :
    from keras import Model
    from keras.engine.saving import model_from_json
    from keras.layers import GlobalAveragePooling2D, Dense
    from keras.models import load_model
    from keras.preprocessing import image
    import numpy as np
    from keras.applications.resnet50 import preprocess_input
    from keras.applications.resnet50 import decode_predictions
    img_width, img_height = 300, 300

    '''
    def load_image(img_path, show=False):
        img = image.load_img(img_path, target_size=(300,300))
        img_tensor = image.img_to_array(img)                    # (height, width, channels)
        img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
        img_tensor /= 255.                                      # imshow expects values in the range [0, 1]
        return img_tensor
    '''

    # load the model we saved, also, according to the results from the Two_Class model , if the result passes the
    #the threshold defined for it,
   # C:\Users\alipkine\PycharmProjects\Test\checkpoints\Two_Classes\ResNet50_model.h5
   # modelPath = "./checkpoints/" + modelType + "/" + "ResNet50_model.h5"
    modelPath = "./checkpoints/" + modelType + "/" + "ResNet50_model.h5"
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, modelPath)



    model = load_model(my_file)
    img = image.load_img(img_path, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    '''
    ##restore and load
    json_file = open("./model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    
    model = model_from_json(loaded_model_json)
    
    model.load_weights("./weights.h5")
    
    model.compile(loss='mean_squared_error', optimizer="RMSprop")
    predicts = model.predict(x)
    #print(predicts[0])
    '''
    return preds