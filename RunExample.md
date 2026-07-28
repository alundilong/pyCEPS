### Environment Setup
```
conda activate epbridge-af
cd pyCEPS
```

### Convert data with ecg included
```
pyceps --system "carto" --study-repository "tests\Export_VT-dummy-02_14_2024-11-23-36.zip" --convert --visualize --save-study --keep-ecg
```

### Run visulization
```
python example\mytest.py
```