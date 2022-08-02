# Traffic-speed-prediction

We have added all the baseline models results and codes to our GitHub, inluding ST-GRAT, GMAN, AST-GAT, Etc! note, we did not add the ST-GRAT results to our paper because the prediction precision of ST-GRAT (implemented by PyTorch, torch==1.6.0) is further lower than GMAN. if need, we can added it to paper!!!  

## 注意事项

<font face="微软雅黑" >需要注意的是，需要根据requirements.txt文件中指示的包进行安装，才能正常的运行程序！！！</font>
>* 首先，使用conda创建一个虚拟环境，如‘conda create traffic_speed’；  
> * 激活环境，conda activate traffic_speed；  
> * 安装环境，需要安装的环境已经添加在requirements.txt中，可以用conda安装，也可以使用pip安装，如：conda install tensorflow==1.12.0；  
> * 如果安装的是最新的tensorflow环境，也没问题，tensorflow的包按照以下方式进行导入即可：import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()；  
> * 点击 run_train.py文件即可运行代码。
> * 需要注意的是，我们在tensorflow的1.12和1.14版本环境中都可以运行
---

## Experimental Results
### HA (Multi-steps)
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |6.185242 |6.185242 |6.185242 |6.185242 |6.185242 |6.185242 |
| RMSE           |10.139710|10.139710|10.139710|10.139710|10.139710|10.139710|
| MAPE           |0.126192 |0.126192 |0.126192 |0.126192 |0.126192 |0.126192 |
| R              |0.941854 |0.941854 |0.941854 |0.941854 |0.941854 |0.941854 |
| R<sup>2</sup>  |0.886221 |0.886221 |0.886221 |0.886221 |0.886221 |0.886221 | 
---
### ARIMA (Multi-steps)
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.883667 |6.046000 |6.104512 |6.374540 |6.360256 |6.168883 |
| RMSE           |9.429440 |9.798609 |9.769539 |10.209594|10.030069|9.769304 |
| MAPE           |0.102238 |0.159162 |0.130914 |0.110670 |0.129478 |0.131120 |
| R              |0.941224 |0.937721 |0.937789 |0.930736 |0.933817 |0.937160 |
| R<sup>2</sup>  |0.885876 |0.879284 |0.879403 |0.866113 |0.871992 |0.878266 |
---
### SVM (Multi-steps)
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.622419 |5.694858 |5.636928 |5.902129 |5.898720 |5.929169 |
| RMSE           |9.541193 |9.459830 |9.366811 |9.714313 |9.744125 |9.761787 |
| MAPE           |0.111848 |0.114599 |0.126784 |0.138657 |0.142691 |0.127152 |
| R              |0.948368 |0.949696 |0.950375 |0.947028 |0.946775 |0.946549 |
| R<sup>2</sup>  |0.898497 |0.901055 |0.902324 |0.895883 |0.895211 |0.894915 | 
---
### LSTM (Multi-steps)
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.517776 |5.632012 |5.777946 |5.946635 |6.041769 |6.079495 |
| RMSE           |9.125115 |9.284576 |9.433199 |9.641906 |9.626469 |9.586535 |
| MAPE           |0.133428 |0.140966 |0.126444 |0.119835 |0.122028 |0.134512 |
| R              |0.952999 |0.951341 |0.949730 |0.946881 |0.947458 |0.947507 |
| R<sup>2</sup>  |0.908157 |0.904874 |0.901881 |0.896313 |0.897537 |0.897657 | 
---
### Bi-LSTM (Multi-steps)
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.524607 |5.632932 |5.771882 |5.954062 |6.055177 |6.096319 |
| RMSE           |9.129195 |9.285857 |9.423597 |9.640355 |9.636107 |9.591586 |
| MAPE           |0.132028 |0.140429 |0.127086 |0.122740 |0.127745 |0.141035 |
| R              |0.953077 |0.951397 |0.949857 |0.946916 |0.947363 |0.947457 |
| R<sup>2</sup>  |0.908075 |0.904848 |0.902081 |0.896346 |0.897331 |0.897549 |
---
### FI-RNNs (Multi-steps)
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.520539 |5.626097 |5.768340 |5.932466 |6.028442 |6.048296 |
| RMSE           |9.116093 |9.267610 |9.432268 |9.622239 |9.603523 |9.569430 |
| MAPE           |0.137907 |0.144544 |0.130363 |0.123199 |0.129686 |0.140039 |
| R              |0.953136 |0.951567 |0.949828 |0.947121 |0.947781 |0.947735 |
| R<sup>2</sup>  |0.908339 |0.905221 |0.901901 |0.896736 |0.898025 |0.898022 |  
---
### PSPNN (Multi-steps)
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.386255 |5.468801 |5.567571 |5.716054 |5.768782 |5.749586 |
| RMSE           |8.880815 |9.022358 |9.145341 |9.307195 |9.271415 |9.167632 |
| MAPE           |0.130217 |0.135699 |0.120082 |0.114041 |0.116743 |0.128589 |
| R              |0.955524 |0.954207 |0.952829 |0.950642 |0.951668 |0.952150 |
| R<sup>2</sup>  |0.913009 |0.910171 |0.907778 |0.903387 |0.904956 |0.906406 | 
---
### MDL (Multi-steps)
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.429035 |5.509909 |5.627575 |5.784230 |5.813673 |5.804645 |
| RMSE           |8.916788 |9.076988 |9.176666 |9.381263 |9.304234 |9.256170 |
| MAPE           |0.130555 |0.134097 |0.120055 |0.115990 |0.117240 |0.129795 |
| R              |0.955434 |0.953698 |0.952556 |0.949963 |0.951238 |0.951537 |
| R<sup>2</sup>  |0.912303 |0.909080 |0.907145 |0.901843 |0.904282 |0.904590 |  
---
### T-GCN (Multi-steps)  
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.670292 |5.675068 |5.746703 |5.863256 |5.888195 |5.831183 |
| RMSE           |9.134161 |9.173527 |9.245162 |9.387154 |9.317363 |9.195807 |
| MAPE           |0.138232 |0.141509 |0.124293 |0.118078 |0.119514 |0.132048 |
| R              |0.953061 |0.952621 |0.951832 |0.949719 |0.950864 |0.951782 |
| R<sup>2</sup>  |0.907975 |0.907136 |0.905754 |0.901720 |0.904011 |0.905830 | 
---
### AST-GAT (Multi-steps)
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.248924 |5.258951 |5.329265 |5.428566 |5.421416 |5.314834 |
| RMSE           |8.705578 |8.784430 |8.828416 |8.943468 |8.809244 |8.712925 |
| MAPE           |0.124102 |0.128212 |0.114900 |0.110572 |0.110653 |0.121733 |
| R              |0.957302 |0.956514 |0.956069 |0.954439 |0.956152 |0.956983 |
| R<sup>2</sup>  |0.916408 |0.914847 |0.914059 |0.910791 |0.914195 |0.915460 | 
---
### GMAN (Multi-steps)  
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.233438 |5.208744 |5.256062 |5.329036 |5.347667 |5.204790 |
| RMSE           |8.730351 |8.795372 |8.797104 |8.908348 |8.818618 |8.598270 |
| MAPE           |0.130036 |0.131432 |0.116220 |0.107743 |0.111887 |0.117915 |
| R              |0.957150 |0.956506 |0.956505 |0.954913 |0.956238 |0.958076 |
| R<sup>2</sup>  |0.915932 |0.914634 |0.914668 |0.911490 |0.914013 |0.917670 | 
---
### GMAN_1 (without decoder on spatiotemporal attention)  
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.234585 |5.178617 |5.211098 |5.287373 |5.322027 |5.223792 |
| RMSE           |8.734820 |8.744925 |8.779705 |8.879185 |8.817018 |8.640688 |
| MAPE           |0.130630 |0.128092 |0.114170 |0.106051 |0.110179 |0.120951 |
| R              |0.957045 |0.956970 |0.956621 |0.955153 |0.956184 |0.957628 |
| R<sup>2</sup>  |0.915846 |0.915611 |0.915005 |0.912069 |0.914044 |0.916856 | 
---
### ST-GRAT (Multi-steps)  
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.126567 |5.224280 |5.335337 |5.456082 |5.562169 |5.662242 |
| RMSE           |8.719842 |8.848616 |8.980233 |9.120206 |9.243639 |9.359533 |
| MAPE           |0.117111 |0.119548 |9.243639 |0.124147 |0.126001 |0.127665 |
| R              |0.957088 |0.956256 |0.126001 |0.954598 |0.953828 |0.953095 |
| R<sup>2</sup>  |0.915784 |0.913271 |0.910662 |0.907852 |0.905335 |0.902939 | 
---
### STGIN (Multi-steps) 
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.175827 |5.100160 |5.149714 |5.222380 |5.245451 |5.150738 |
| RMSE           |8.644908 |8.640150 |8.701153 |8.819650 |8.724352 |8.527315 |
| MAPE           |0.126175 |0.127834 |0.112100 |0.104818 |0.108805 |0.117945 |
| R              |0.957921 |0.957968 |0.957378 |0.955765 |0.957101 |0.958707 |
| R<sup>2</sup>  |0.917550 |0.917624 |0.916518 |0.913230 |0.915819 |0.919006 |  
---
### STGIN_1 (Multi-steps) without semantic transformation
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.177275 |5.109780 |5.187932 |5.239958 |5.257546 |5.156742 |
| RMSE           |8.631874 |8.640737 |8.729155 |8.806985 |8.720966 |8.515376 |
| MAPE           |0.132412 |0.131180 |0.117357 |0.109338 |0.113217 |0.120528 |
| R              |0.958046 |0.957964 |0.957082 |0.955788 |0.957056 |0.958787 |
| R<sup>2</sup>  |0.917799 |0.917613 |0.915979 |0.913479 |0.915884 |0.919233 | 
---
### STGIN_2 (Multi-steps) uses an encoder of GMAN to replace the of ST-Block STGIN
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.195487 |5.116568 |5.174414 |5.246917 |5.274146 |5.178238 |
| RMSE           |8.718395 |8.693000 |8.744741 |8.864868 |8.775015 |8.614857 |
| MAPE           |0.127035 |0.129896 |0.113813 |0.105365 |0.108400 |0.119232 |
| R              |0.957350 |0.957625 |0.957099 |0.955481 |0.956771 |0.958061 |
| R<sup>2</sup>  |0.916143 |0.916614 |0.915679 |0.912338 |0.914838 |0.917335 | 
---
### STGIN_3 (Multi-steps) dynamic step-by-step method to replace the generative inference of STGIN
|评价指标         |6-1 steps|6-2 steps|6-3 steps|6-4 steps|6-5 steps|6-6 steps|
|  ----          | ----    |  ----   |  ----   |----     |----     |----     |
| MAE            |5.182895 |5.167289 |5.197474 |5.254837 |5.308890 |5.164660 |
| RMSE           |8.666809 |8.727748 |8.737943 |8.846064 |8.761161 |8.555215 |
| MAPE           |0.126229 |0.129717 |0.114406 |0.107089 |0.108753 |0.117827 |
| R              |0.957731 |0.957168 |0.957062 |0.955487 |0.956708 |0.958486 |
| R<sup>2</sup>  |0.917151 |0.915942 |0.915812 |0.912723 |0.915129 |0.918493 | 
---
## 代码更正
##### 如果你想保证模型的精准度更高，请将 bridge.py 中的代码，改为以下代码 (block set to 1， and input length set to 12)
* 新版STGIN映射到STGIN_4权重weights/参数上，以此类推，STGIN_3映射到STGIN_7权重weights/参数上，
 
            # Blocks
            for i in range(self.num_blocks):
                with tf.variable_scope("num_blocks_{}".format(i)):
                    # Multihead Attention
                    X_Q = multihead_attention(queries=X_Q, # future time steps
                                            keys=X_P,    # historical time steps
                                            values= X,   # historical inputs
                                            num_units=self.hidden_units,
                                            num_heads= self.num_heads, # self.num_heads
                                            dropout_rate=self.dropout_rate,
                                            is_training=self.is_training)
                    # Feed Forward
                    X_Q = feedforward(X_Q, num_units=[4 * self.hidden_units, self.hidden_units])
        X = tf.reshape(X_Q,shape=[-1, self.site_num, self.output_length, self.hidden_units])
---