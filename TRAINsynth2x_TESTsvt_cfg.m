function cfg=TRAINsynth2x_TESTsvt_cfg

cfg=struct();
cfg.train='synth2x';
cfg.train_bg='msrc';
cfg.train_type='char';

cfg.test='svt';
cfg.lex='lex';
cfg.lex0='lex';
cfg.test_type='';

cfg.has_par=0;