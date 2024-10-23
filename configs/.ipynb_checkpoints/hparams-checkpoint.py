
## The cuurent hyper-parameters values are not necessarily the best ones for a specific risk.
def get_hparams_class(dataset_name):
    """Return the algorithm class with the given name."""
    if dataset_name not in globals():
        raise NotImplementedError("Dataset not found: {}".format(dataset_name))
    return globals()[dataset_name]


class HAR():
    def __init__(self):
        super(HAR, self).__init__()
        self.train_params = {
                'num_epochs': 50,
                'batch_size': 32,
                'weight_decay': 1e-4,

        }
        self.alg_hparams = {
            'RAINCOAT':       {'learning_rate':5e-4,     'src_cls_loss_wt': 0.5,    'domain_loss_wt': 0.5},
            'DANN':         {'learning_rate': 1e-2, 'src_cls_loss_wt': 9.74, 'domain_loss_wt': 5.43},
            'Deep_Coral':   {'learning_rate': 5e-3, 'src_cls_loss_wt': 8.67, 'coral_wt': 0.44},
            'DDC':          {'learning_rate': 5e-3, 'src_cls_loss_wt': 6.24, 'domain_loss_wt': 6.36},
            'HoMM':         {'learning_rate': 1e-3, 'src_cls_loss_wt': 2.15, 'domain_loss_wt': 9.13},
            'CoDATS':       {'learning_rate': 1e-3, 'src_cls_loss_wt': 6.21, 'domain_loss_wt': 1.72},
            'DSAN':         {'learning_rate': 5e-4, 'src_cls_loss_wt': 1.76, 'domain_loss_wt': 1.59},
            'AdvSKM':       {'learning_rate': 5e-3, 'src_cls_loss_wt': 3.05, 'domain_loss_wt': 2.876},
            'MMDA':         {'learning_rate': 1e-3, 'src_cls_loss_wt': 6.13, 'mmd_wt': 2.37, 'coral_wt': 8.63, 'cond_ent_wt': 7.16},
            'CDAN':         {'learning_rate': 1e-2, 'src_cls_loss_wt': 5.19, 'domain_loss_wt': 2.91, 'cond_ent_wt': 1.73},
            "AdaMatch":      {'learning_rate': 3e-3,     'tau': 0.9, 'max_segments': 5, 'jitter_scale_ratio': 0.01, 'jitter_ratio': 0.2},
            'DIRT':         {'learning_rate': 5e-4, 'src_cls_loss_wt': 7.00, 'domain_loss_wt': 4.51, 'cond_ent_wt': 0.79, 'vat_loss_wt': 9.31},
            "DANCE":        {'learning_rate': 1e-3,    'momentum': 0.5, 'eta': 0.05, "thr": 1.71,   "margin": 0.5, 'temp': 0.05}
        }


class EEG():
    def __init__(self):
        super(EEG, self).__init__()
        self.train_params = {
                'num_epochs': 40,
                'batch_size': 128,
                'weight_decay': 1e-4,

        }
        self.alg_hparams = {
            'RAINCOAT':       {'learning_rate':0.002,     'src_cls_loss_wt': 0.5,    'domain_loss_wt': 0.5},
             "AdaMatch":      {'learning_rate': 0.0005,     'tau': 0.9, 'max_segments': 5, 'jitter_scale_ratio': 0.01, 'jitter_ratio': 0.2},
            'DANN':         {'learning_rate': 0.0005,   'src_cls_loss_wt': 8.30,    'domain_loss_wt': 0.324, },
            'Deep_Coral':   {'learning_rate': 0.0005,   'src_cls_loss_wt': 9.39,    'coral_wt': 0.19, },
            'DDC':          {'learning_rate': 0.0005,   'src_cls_loss_wt': 2.951,   'domain_loss_wt': 8.923, },
            'HoMM':         {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.197,   'domain_loss_wt': 1.102, },
            'CoDATS':       {'learning_rate': 0.01,     'src_cls_loss_wt': 9.239,   'domain_loss_wt': 1.342, },
            'DSAN':         {'learning_rate': 0.001,    'src_cls_loss_wt': 6.713,   'domain_loss_wt': 6.708, },
            'AdvSKM':       {'learning_rate': 0.0005,   'src_cls_loss_wt': 2.50,    'domain_loss_wt': 2.50, },
            'MMDA':         {'learning_rate': 0.0005,   'src_cls_loss_wt': 4.48,    'mmd_wt': 5.951, 'coral_wt': 3.36, 'cond_ent_wt': 6.13, },
            'CDAN':         {'learning_rate': 0.001,    'src_cls_loss_wt': 6.803,   'domain_loss_wt': 4.726, 'cond_ent_wt': 1.307, },
            'DIRT':         {'learning_rate': 0.005,    'src_cls_loss_wt': 9.183,   'domain_loss_wt': 7.411, 'cond_ent_wt': 2.564, 'vat_loss_wt': 3.583, },
            "DANCE":        {'learning_rate': 1e-3,    'momentum': 0.5, 'eta': 0.05, "thr": 1.71,   "margin": 0.5, 'temp': 0.05}
        }


class WISDM():
    def __init__(self):
        super(WISDM, self).__init__()
        self.train_params = {
                'num_epochs': 50,
                'batch_size': 64,
                'weight_decay': 1e-4,

        }
        self.alg_hparams = {
            'DANN':         {'learning_rate': 1e-3,     'src_cls_loss_wt': 1.613,   'domain_loss_wt': 1.857},
            'Deep_Coral':   {'learning_rate': 0.005,    'src_cls_loss_wt': 8.876,   'coral_wt': 5.56},
            'DDC':          {'learning_rate': 1e-3,     'src_cls_loss_wt': 7.01,    'domain_loss_wt': 7.595},
            'HoMM':         {'learning_rate': 1e-3,     'src_cls_loss_wt': 0.1913,  'domain_loss_wt': 4.239},
            'CoDATS':       {'learning_rate': 1e-3,     'src_cls_loss_wt': 7.187,   'domain_loss_wt': 6.439},
            'DSAN':         {'learning_rate': 1e-3,     'src_cls_loss_wt': 0.1,     'domain_loss_wt': 0.1},
            'AdvSKM':       {'learning_rate': 3e-4,     'src_cls_loss_wt': 3.05,    'domain_loss_wt': 2.876},
            'MMDA':         {'learning_rate': 1e-3,     'src_cls_loss_wt': 0.1,     'mmd_wt': 0.1, 'coral_wt': 0.1, 'cond_ent_wt': 0.4753},
            "AdaMatch":      {'learning_rate': 3e-3,     'tau': 0.9, 'max_segments': 5, 'jitter_scale_ratio': 0.01, 'jitter_ratio': 0.2},
            'CDAN':         {'learning_rate': 1e-3,     'src_cls_loss_wt': 9.54,    'domain_loss_wt': 3.283,        'cond_ent_wt': 0.1},
            'DIRT':         {'learning_rate': 1e-3,     'src_cls_loss_wt': 0.5,     'domain_loss_wt': 0.5,          'cond_ent_wt': 0.1, 'vat_loss_wt': 0.1},
            'RAINCOAT':       {'learning_rate':1e-3,     'src_cls_loss_wt': 0.5,    'domain_loss_wt': 0.5},
            "DANCE":        {'learning_rate': 1e-3,    'momentum': 0.5, 'eta': 0.05, "thr": 1.71,   "margin": 0.5, 'temp': 0.05}
        }



class HHAR_SA():
    def __init__(self):
        super(HHAR_SA, self).__init__()
        self.train_params = {
                'num_epochs': 40,
                'batch_size': 32,
                'weight_decay': 1e-4,
        }
        self.alg_hparams = {
            'RAINCOAT':       {'learning_rate':0.001,     'src_cls_loss_wt': 0.5,    'domain_loss_wt': 0.5},
            'DANN':         {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.9603,  'domain_loss_wt':0.9238},
            'Deep_Coral':   {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.05931, 'coral_wt': 8.452},
            'DDC':          {'learning_rate': 0.01,     'src_cls_loss_wt':  0.1593, 'domain_loss_wt': 0.2048},
            'HoMM':         {'learning_rate':0.001,     'src_cls_loss_wt': 0.2429,  'domain_loss_wt': 0.9824},
            'CoDATS':       {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.5416,  'domain_loss_wt': 0.5582},
            'DSAN':         {'learning_rate': 0.005,    'src_cls_loss_wt':0.4133,   'domain_loss_wt': 0.16},
            'AdvSKM':       {'learning_rate': 0.001,    'src_cls_loss_wt': 0.4637,  'domain_loss_wt': 0.1511},
            'MMDA':         {'learning_rate': 0.001,    'src_cls_loss_wt': 0.9505,  'mmd_wt': 0.5476,           'cond_ent_wt': 0.5167,  'coral_wt': 0.5838, },
            'CDAN':         {'learning_rate': 0.001,    'src_cls_loss_wt': 0.6636,  'domain_loss_wt': 0.1954,   'cond_ent_wt':0.0124},
             "AdaMatch":      {'learning_rate': 3e-3,     'tau': 0.9, 'max_segments': 5, 'jitter_scale_ratio': 0.01, 'jitter_ratio': 0.2},
            'DIRT':         {'learning_rate': 0.001,    'src_cls_loss_wt': 0.9752,  'domain_loss_wt': 0.3892,   'cond_ent_wt': 0.09228,  'vat_loss_wt': 0.1947},
            "DANCE":        {'learning_rate': 1e-3,    'momentum': 0.5, 'eta': 0.05, "thr": 1.71,   "margin": 0.5, 'temp': 0.05}
        }


class Boiler():
    def __init__(self):
        super(Boiler, self).__init__()
        self.train_params = {
                'num_epochs': 30,
                'batch_size': 32,
                'weight_decay': 1e-4,
        }
        self.alg_hparams = {
            'RAINCOAT':         {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.9603,  'domain_loss_wt':0.9238},
            'DANN':         {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.9603,  'domain_loss_wt':0.9238},
            'Deep_Coral':   {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.05931, 'coral_wt': 8.452},
            'DDC':          {'learning_rate': 0.01,     'src_cls_loss_wt':  0.1593, 'domain_loss_wt': 0.2048},
            'HoMM':         {'learning_rate':0.001,     'src_cls_loss_wt': 0.2429,  'domain_loss_wt': 0.9824},
            'CoDATS':       {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.5416,  'domain_loss_wt': 0.5582},
            'DSAN':         {'learning_rate': 0.005,    'src_cls_loss_wt':0.4133,   'domain_loss_wt': 0.16},
            'AdvSKM':       {'learning_rate': 0.001,    'src_cls_loss_wt': 0.4637,  'domain_loss_wt': 0.1511},
            'MMDA':         {'learning_rate': 0.001,    'src_cls_loss_wt': 0.9505,  'mmd_wt': 0.5476,           'cond_ent_wt': 0.5167,  'coral_wt': 0.5838, },
            'CDAN':         {'learning_rate': 0.001,    'src_cls_loss_wt': 0.6636,  'domain_loss_wt': 0.1954,   'cond_ent_wt':0.0124},
            'DIRT':         {'learning_rate': 0.001,    'src_cls_loss_wt': 0.9752,  'domain_loss_wt': 0.3892,   'cond_ent_wt': 0.09228,  'vat_loss_wt': 0.1947},
            "DANCE":        {'learning_rate': 1e-3,    'momentum': 0.5, 'eta': 0.05, "thr": 1.71,   "margin": 0.5, 'temp': 0.05},
            "OVANet":       {'learning_rate': 1e-3,    'sgd_momentum': 0.9, 'momentum': 0.00, 'min_step': 10000, 'eta': 0.05, 'thr': 1.09,   'margin': 0.5, 'temp': 0.05, 'multi': 0.1},
            "AdaMatch":      {'learning_rate': 3e-3,     'tau': 0.9, 'max_segments': 5, 'jitter_scale_ratio': 0.01, 'jitter_ratio': 0.2},
        }


class FutureCrop():
    def __init__(self):
        super(FutureCrop, self).__init__()
        self.train_params = {
                'num_epochs': 30,
                'batch_size': 32,
                'weight_decay': 1e-4,
        }
        self.alg_hparams = {
            'RAINCOAT':         {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.9603,  'domain_loss_wt':0.9238},
            'DANN':         {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.9603,  'domain_loss_wt':0.9238},
            'Deep_Coral':   {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.05931, 'coral_wt': 8.452},
            'DDC':          {'learning_rate': 0.01,     'src_cls_loss_wt':  0.1593, 'domain_loss_wt': 0.2048},
            'HoMM':         {'learning_rate':0.001,     'src_cls_loss_wt': 0.2429,  'domain_loss_wt': 0.9824},
            'CoDATS':       {'learning_rate': 0.0005,   'src_cls_loss_wt': 0.5416,  'domain_loss_wt': 0.5582},
            'DSAN':         {'learning_rate': 0.005,    'src_cls_loss_wt':0.4133,   'domain_loss_wt': 0.16},
            'AdvSKM':       {'learning_rate': 0.001,    'src_cls_loss_wt': 0.4637,  'domain_loss_wt': 0.1511},
            'MMDA':         {'learning_rate': 0.001,    'src_cls_loss_wt': 0.9505,  'mmd_wt': 0.5476,           'cond_ent_wt': 0.5167,  'coral_wt': 0.5838, },
            'CDAN':         {'learning_rate': 0.001,    'src_cls_loss_wt': 0.6636,  'domain_loss_wt': 0.1954,   'cond_ent_wt':0.0124},
            'DIRT':         {'learning_rate': 0.001,    'src_cls_loss_wt': 0.9752,  'domain_loss_wt': 0.3892,   'cond_ent_wt': 0.09228,  'vat_loss_wt': 0.1947},
            "DANCE":        {'learning_rate': 1e-3,    'momentum': 0.5, 'eta': 0.05, "thr": 1.71,   "margin": 0.5, 'temp': 0.05},
            "OVANet":       {'learning_rate': 1e-3,    'sgd_momentum': 0.9, 'momentum': 0.00, 'min_step': 10000, 'eta': 0.05, 'thr': 1.09,   'margin': 0.5, 'temp': 0.05, 'multi': 0.1},
            "AdaMatch":      {'learning_rate': 3e-3,     'tau': 0.9, 'max_segments': 5, 'jitter_scale_ratio': 0.01, 'jitter_ratio': 0.2},
        }
