# singing-database-maker

## Preface

High quality data is always a problem of singing voice synthesis. And it's really laborious to make a database from scrach. We hope AI can make the process a lot easier, so every music lover can make his own synthesised song.

Hopefully, there are just tools satisfy our needs. We combine them and a tool to ease the process.Thanks to all the contibuters of these grate researches. We list them below, so you can go and check their work:

> [1] Sangeun Kum et al. “Semi-supervised learning using teacher-student models for vocal melody extraction”. In: Proc. International Society of Music Information Retrieval Conference (ISMIR). 2020.
>
> [2] Xianming Li. XMNLP: A Lightweight Chinese Natural Language Processing Toolkit. https://github.com/SeanLee97/ xmnlp. 2018.
>
> [3] Kilian Schulze-Forster et al. “Phoneme Level Lyrics Alignment and Text-Informed Singing Voice Separation”. In: IEEE/ACM Transactions on Audio, Speech, and Language Processing 29 (2021), pp. 2382–2395. DOI: 10.1109/TASLP.2021. 3091817.



## Input and Output

Notice: The project now support English songs only, with Chinese support in  early development. The key is Phoneme Level Lyrics Alignment module, we assume we can deal with it this summer.

List here so you can have a genneral idea of whether the project suits your needs.

Input: songs and their .lrc format lyrics.

Output: 

- songs devided into slices according to lyrics sentences
- phoneme and word list, with the time their appear in the slice
- a midi file generated by Semi-supervised AI network

We plan to add:

- musicXML generator
- Chinese support
- more precise midi file
- an synthesised example using the database

## Steps

### general introduction

suppose you have a song called foo. the processed database folder will be like this: (only list the tools you will use)

```shell
 - origin
 	- foo.wav
 	- foo.lrc
 - processed_data
 	- vocal
 	- slice
 		- foo00150019
 			foo00150019.wav
 			foo00150019.txt
 		- ...
 	- pitch
 		- pitch_foo00150019
 		- ...
 	- midi
 		- foo00150019.mid
 		- ...
 	- align
 		- foo00150019
 			- phoneme_onsets
 				- foo00150019.txt
 			- word_onsets
 				- foo00150019.txt
 - utils
 	- english-align
 		- phoneme_from_word
 		- make_phoe.py
 	- melodyExtraction
 		- gen_freq.py
 	- vocal-extraction
 	- config.py
    - song_cutter.py
    - demix_vocal.py
    - gen_midi.py
    - make_Midi.py
    - make_lab.py (not finished)
    - make_musicxml.py (not finished)
    - delete_useless.py (not tested)
    - missing.txt (generate after align)
```



### environment preparation

When dealing with mutiple AI projects, it will make your life much easier to set up the environment properly at first step. We've had a hard time dealing with all of this, and we found you can use the project on your own pc if you set correctly.

1. install a python virtual environment manager

    We use recommand conda, and we take this as an example

2. crate environment for song-cutter and those non-AI program

    ```shell
    conda create -n music-dealer
    ```

    ### not finished, next update on 6.28

    

### seperate the song

### demix the slice

### generate midi notes and make midi

### generate phoneme Level Lyrics Alignment



## License and acknowledgement

The whole project is under MIT License, all the projects we used in this project are under their own license.

We do not guarantee the quality of dataset, and before using any data, you must have the appropriate copyright permission.



