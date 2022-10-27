# Idiom Recognition Module (IR) [ UNIGE ]

**SCOPE:** real-time automatic Language Recognition - outputs the language of the current speaker by analyzing an input audio file.

# Module Repository
[GitLab UNIMORE](https://git.hipert.unimore.it/fractal/idiomrecognition/)\
[AITEK Repo](https://nextcloud.aitek.it/s/fLdfaSCcWBTEBfj?path=%2FImplementations%2FIdiom%20Recognition%20-%20IR/)

## Quick Start How-To
- Download the IR Module files and install the required packages [see the guidelines below]
- Download the desired language models [see the guidelines below]
- For a quick reference on how to use pyBabl, use the built-in help: `python pyBabl.py -h` 
- When you launch the app for the first time, use the option `-s` to correctly setup your microphone.\
e.g, `python pyBabl.py -s` or `python pyBabl.py --setup`\
If you are not sure about which hardware to choose, go for the _default_ one.
- To recognize the language you need to say a hot-word. Currently supported hot-words are:
    - italiano | benvenuto [ _ITALIAN_ ]
    - english | english [ _ENGLISH_ ]
    - deutsch | willkommen [ _GERMAN_ ]
    - français | bienvenue [ _FRENCH_ ]
    - español | bienvenidos [ _SPANISH_ ]

## Basic commands

- To start the recognition in live mode, run: `python pyBabl.py`
- To start the recognition on a pre-recorded audio file, run: `python pyBabl.py -f "<file-name>"`
- To record an audio file, use: `python pyBabl.py -r` or `python pyBabl.py --record`
- You can also specify the extension by adding the option: `-e "wav"` [default is "wav"]
- To test a pre-recorded audio file, use:  `python pyBabl.py -t -l LANG -n SAMPLE` or `python pyBabl.py --test --lang LANG -num SAMPLE` (for other usage examples, see below)

See Section _Usage Examples_ below for further details.

## Command Line Arguments

usage: `pyBabl.py [-h] [-d] [-t] [-r] [-f FILE] [-l {ITA,ENG,GER,FRA,SPA}] [-n NUM] [-e {wav,raw,aiff,flac}] [-s]`

optional arguments:

`-h, --help`            show this help message and exit\
`-d, --debug`           enable debug mode\
`-t, --test`            enable test on pre-recorded file\
`-r, --rec`             record audio file\
`-f FILE, --file FILE`            path to audio file to test\
`-l {ITA,ENG,GER,FRA,SPA}, --lang {ITA,ENG,GER,FRA,SPA}` select test file language\
`-n NUM, --num NUM`     select test file number\
`-e {wav,raw,aiff,flac}, --ext {wav,raw,aiff,flac}` select file extension\
`-s, --setup`           launch this for hardware setup

##### Usage Examples
- LIVE MODE\
`python pyBabl.py`      runs the live language recognition mode

- TEST MODE\
`python pyBabl.py -t`   runs the default test on file _test\_ITA\_1.wav_
`python pyBabl.py -t -l "ENG" -n "2"` tests recognition on file _test\_ENG\_2.wav_
`python pyBabl.py -t -f "test_SPA_3"` tests recognition on file _test\_FRA\_3.wav_

- RECORD MODE\
`python pyBabl.py -r`   records a file with a random name (for successive recordings)
`python pyBabl.py -r -f "test_SPA_3"` tests recognition on file _test\_FRA\_4.wav_

## General Info & Installation Instructions

**Test audio files** can be pre-recorded using the _Record Mode_ and must be located in `./audio/test/test_LANG_N.EXT` [e.g., `./audio/test/test_ENG_1.wav`] to work.

**Language Models** can be found [here](https://alphacephei.com/vosk/models) and must be located in `./models/model_LANG/*` [e.g., `./models/model_ENG/*`] to work. Currently supported models are already available inside the _./models/*_ folder and can also be downloaded here:
- [Italian Model](https://alphacephei.com/vosk/models/vosk-model-small-it-0.4.zip)
- [English Model](https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip)
- [German Model](https://alphacephei.com/vosk/models/vosk-model-small-de-0.15.zip)
- [French Model](https://alphacephei.com/vosk/models/vosk-model-small-fr-0.22.zip)
- [Spanish Model](https://alphacephei.com/vosk/models/vosk-model-small-es-0.22.zip)

**Speech Recognition** tools are from the _PyPi_ SpeechRecognition project.\
See the [PyPi Official Website](https://pypi.org/project/SpeechRecognition/) for reference.\
`pip install SpeechRecognition`

ALR is based on the open-source speech recognition toolkit _Vosk_.\
See [Vosk Official Website](https://alphacephei.com/vosk) for reference.\
`pip install vosk`\
Some platforms are not fully supported by pip, for example on arm64 you have to install from released wheels (available in the _resources_ folder):
- resources\vosk-0.3.42-py3-none-linux_aarch64.whl

Language models are available [here](https://alphacephei.com/vosk/models)

The preferred hardware **Microphone** can be selected using the _sounddevice_ package\
`pip install sounddevice`

The **Speech Utils** custom library is based on the _pygame_ and _PyAudio_ libraries\
`pip install pygame`\
Unfortunately _PyAudio_ is not available for Python>3.6. 

**WINDOWS**\
Unofficial wheels for Windows are distributed [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) by UCI, Irvine.
- Python 3.10: _PyAudio-0.2.11-cp310-cp310-win_amd64.whl_ [win64 version]
- Python 3.8: _PyAudio-0.2.11-cp38-cp38-win_amd64.whl_ [win64 version]

**LINUX**
- sudo apt install python3-pyaudio
oppure, in caso di errore, provare:
- Python 3.8 _PyAudio-0.2.11-cp38-cp38-linux_x86_64.whl_ [linux version] _* see below for wheel generation_ \

**ARM64**
- python3-pyaudio_0.2.11-1.1build1_arm64.deb

Wheels can be also found in the pkg dir and installed by running:\
`pip install <wheel_path>` [Python _wheel_ package required]

_Note: Originally developed with Python 3.10.1. Now compatible with Python 3.8._

### Package Requirements Wrap-up:
- SpeechRecognition==3.8.1
- vosk==0.3.32
- pygame==2.1.2
- PyAudio @ file: .\wheels\PyAudio-0.2.11-cpXX-cpXX-YYY_amd64.whl 
- sounddevice==0.4.4

### To install PyAudio and generate a wheel for Linux systems:
`sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 python3-pyaudio`\
`pip install pyaudio`

## I/O Utils
Added I/O Utils (_ioUtils.py_) to support REST API and socket programming. [ _under development_ ]
