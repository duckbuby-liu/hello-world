import sys
import json
from GUI_Mainwindowedition_6 import Ui_MainWindow
from PyQt5.QtWidgets import *

class Mymaingui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Mymaingui, self).__init__(parent)
        self.setupUi(self)
        self.nextbutton.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        # self.nextbutton.clicked.connect(self.quzhi)
        self.runbutton.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.selectfile.clicked.connect(self.Openflie)
        self.nextbutton.setToolTip("hello/nhello")
        self.modi.currentIndexChanged.connect(self.nni_enable)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.nextbutton.clicked.connect(lambda: self.tabWidget.setTabEnabled(1, True))
        self.runbutton.clicked.connect(lambda: self.tabWidget.setTabEnabled(2, True))
#start to deal with user_para and hyper_para. first we should get the value from user. then create json flies.
        self.runbutton.clicked.connect(self.createjson)

    def createjson(self):
        dic_user_params = {
            'delay_coordinates_delay': 0,
            'prediction_horizon': 49,
            'output_information': True,
            'choose_state_prediction_loss': True,
            'choose_Linf_state_prediction_loss': True,
            'choose_state_encoder_loss': True,
            'choose_input_prediction_loss': True,
            'choose_lin_state_prediction_loss': True,
            'choose_Linf_lin_state_prediction_loss': False,
            'choose_lin_input_prediction_loss': False,
            'choose_dmd_loss': True,
            'choose_l1_reg': True,
            'choose_l2_reg': True,
            'choose_decaying_weights': True,
            'choose_dropout': False,
            'choose_dist_loss': False,
            'dropout_rate': 0.1,
            'regularize_loss': False,
            'regularize_loss_lin': False,
            'train_input_autoencoder_only': False,
            'predict_input': False,
            'initialize_lin_model_random': False,
            'max_num_epochs': 1,
            'patience': 10000,
            'patience_min_diff': 10e-20,
            'use_input_time_delay': False,
            'use_cyclic_learning_rate': True,
            'initialize_zero': False,
            'model_path': 'vanDerPol/',
            'path_to_data': 'data/vanDerPol/vanDerPol_Oszillator',
            'log_loss': True,
            'system_outputs': [
                0,
                1
            ],
            'dim_system_input': 1,
            'is_input_affine': True,
            'concept': 1,
            'save_initial_weights': False,
            'initial_weights': None
        }
        dic_search_space = {
            'opt_alg': {
                '_type': 'choice',
                '_value': [
                    'adam'
                ]
            },
            'learning_rate': {
                '_type': 'choice',
                '_value': [
                    0.0001
                ]
            },
            'learning_rate_max': {
                '_type': 'choice',
                '_value': [
                    0.001,
                    0.1
                ]
            },
            'cylic_leaning_rate_length': {
                '_type': 'choice',
                '_value': [
                    6,
                    12,
                    10
                ]
            },
            'batch_size': {
                '_type': 'choice',
                '_value': [
                    512
                ]
            },
            'dropout_rate': {
                '_type': 'choice',
                '_value': [
                    0.1
                ]
            },
            'dim_lin_system': {
                '_type': 'choice',
                '_value': [
                    9
                ]
            },
            'widths_middle_layer_state_encoder': {
                '_type': 'choice',
                '_value': [
                    '[20, 40, 60]'
                ]
            },
            'widths_middle_layer_state_decoder': {
                '_type': "choice",
                '_value': [
                    '[40, 60, 80]'
                ]
            },
            'alpha_state_prediction_loss': {
                '_type': "choice",
                '_value': [
                    1.0
                ]
            },
            'delta_state_prediction_loss': {
                '_type': 'choice',
                '_value': [
                    0.99
                ]
            },
            'alpha_state_encoder_loss': {
                '_type': 'choice',
                '_value': [
                    1.0
                ]
            },
            'alpha_input_prediction_loss': {
                '_type': 'choice',
                '_value': [
                    1.0
                ]
            },
            'delta_input_prediction_loss': {
                '_type': "choice",
                '_value': [
                    0.99
                ]
            },
            'alpha_lin_state_prediction_loss': {
                '_type': 'choice',
                '_value': [
                    1.0
                ]
            },
            'delta_lin_state_prediction_loss': {
                '_type': 'choice',
                '_value': [
                    0.99
                ]
            },
            'alpha_dmd_loss': {
                '_type': 'choice',
                '_value': [
                    0.1
                ]
            },
            'alphal1': {
                '_type': "choice",
                '_value': [
                    0.000001
                ]
            },
            'alphal2': {
                '_type': 'choice',
                '_value': [
                    0.000001
                ]
            },
            'alpha_input_distance_loss': {
                '_type': 'choice',
                '_value': [
                    1.0
                ]
            },
            'alpha_state_distance_loss': {
                '_type': 'choice',
                '_value': [
                    0.001
                ]
            },
            'Linf_state_prediction_loss_loss': {
                '_type': 'choice',
                '_value': [
                    0.01
                ]
            }
        }
        print(dic_search_space)
        json_user_params = 'D:\\Projektseminar\\DKLc-GUI\\1.json'
        json_search_space = 'D:\\Projektseminar\\DKLc-GUI\\2.json'
        with open(json_user_params, 'w') as fileHandler1:
            json.dump(dic_user_params, fileHandler1, indent=2)
        with open(json_search_space, 'w') as fileHandler2:
            json.dump(dic_search_space, fileHandler2, indent=2)

    def nni_enable(self):
        if self.modi.currentIndex() == 2:
            self.nni_cofi.setEnabled(True)
        else:
            self.nni_cofi.setEnabled(False)


    def Openflie(self):
        params = QFileDialog.getExistingDirectory(self, 'Open file', '/')
        self.path_to_data.setText(params)

    # def quzhi(self):
    #
    #     self.tabWidget.setCurrentIndex(1)
    #     a = self.spinBox_4.value()
    #     print(a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = Mymaingui()
    myWin.show()

    sys.exit(app.exec_())

