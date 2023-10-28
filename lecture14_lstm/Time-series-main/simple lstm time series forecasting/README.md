
# Stacked lstm time series forecasting

Industrial motors are typically monitored by a multitude of sensors. In this problem we are given a dataset containing the vibration sensor measurements from 3 bearings of a large industrial motor(sensor1,sensor2,sensor3). The data looks as follows


|    Sensor 1                |   Sensor 2                |     sensor 3             |
| :--------------------------| :------------------------:| :------------------------|
|1.059999999999999964e+01    | 2.000000000000000000e+01  |2.000000000000000000e+00  |
|1.076121929129393351e+01    | 2.002099867501975083e+01	 |2.992446721473281279e+00  |
|1.091283719706222755e+01	   |2.002399479998403464e+01	 |3.943492791413660825e+00  |
|1.105480022370652904e+01	   |2.000900066995905391e+01	 |4.815117832999165515e+00  |
|1.118706349999511573e+01    |1.997604475803108315e+01   |5.572397726205346125e+00  |
|1.130959078429071951e+01    |1.992517168369108660e+01   |6.184897079911567452e+00  |



our task is to predict the readings from three sensors for the next 500 time points assuming that there is no major change in the functioning of the motor.
