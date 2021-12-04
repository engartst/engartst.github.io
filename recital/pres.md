---
marp: true
title: MIR for Algorithmic Music Composition
author: Stewart Engart
paginate: true
url: stewartengart.com
#theme: uncover
---

<style>
h1, h2, h3, h4{
color: black
}
p
{
    
}
</style>

# Music Information Retrieval Driven Algorithmic Music 

## Stewart Engart

UC Santa Barbara, December 04, 2021

---

## What is MIR?

### Music Information Retrieval

segmentation
analysis

---

## How is MIR being used?

copyright enforcement (royalties, plagarism)
playlist recommendations (mood, emotion, style)
querying by humming, etc.

---


## How has this been applied to composition?

"We propose that problems arise not necessarily due to the sheer volume of decisions and possibilities, but due to a lack of strategic methods to hierarchize decision-making and to interconnect programmatically different strata of sonic experience."

Hackbarth, p 50.

---

### Concatenative Synthesis

1. analysis
2. database
3. unit selection
4. synthesis

Almeida, p 11.

---

### Concatenative Synthesis

"The convention adopted here is that when the result bears little resemblance to the original, then the transformation is more synthesis than effect"

Sturm, p 48.

---

## Results of survey of expert MIR users by Anderson and Knees

1. Surprise and serendipity in recommendation and retrieval are important to support creative work.
2. Users have personal mental images of sound.
3. There is a need for semantic representations of sounds for retrieval, which are not just tags and words but rather reflect those mental images (which can be visual or haptic).
4. Instead of “more of the same” recommendations, desired features are surprise, opposition, individuality, and control over the recommendation process.

---
## Searching a database from Blum, 1999.

1. Simile
2. Acoustical/perceptual features
3. Subjective features
4. Onomatopocia

---

## How did I get here?

---

### Past compostions

|                 				Piece 			               	| Techniques                                          	|
|:------------------------------------:	|-----------------------------------------------------	|
| Tears of Tesla 2: Electric Boogaloo 			 	| analysis of amplitude for visualization             	|
| Come On, America! 	\*		                   	| analysis, formant synthesis, parameter modulation   	|
|  Peace? Through the Night 			           	| time stretched use of pre-existing material         	|
| The Problem with Pandas              	| extraction of rhythmic contours from tape           	|
|  vizual \*			                             	| analysis/re-synthesis, visualization (oscilloscope) 	|
| Je me suis trouvé \*                   	| concatenative synthesis, analysis of sound grains   	|

\* included on recital

---

## Salient features

- Zero crossing rate (ZCR)
- Root mean square (RMS)
- Spectral centroid (brightness) 
- Spectal rolloff (distribution) 
- Harmonicity (vowels, how harmonic) 
- Pitch (first peak)

From Sturm, p. 51.

---

## Clustering

"When face with a set of objects, people often sort them into clusters to reduce information load and facilitate further processing."

Tversky, p 342.

---

Supervised vs. unsupervised
*KONTAKTE* by Stockhausen

---
![bg 75%](kmeans12_cluster3.png)

---

![bg 75%](kmeans12_cluster3_cluster3_withCentroids.png)



---
## Dealing with high dimensions

weighting of features
multiple passes
Principal component analysis (PCA)

---
## Sound design

Querying for a desired sound based off of features rather than manipulation of an audio file to fit.

Implication to source identification.

---

## Referential and iconic sounds

- the isomorphic image (iconic, referential), im-sound.
- the diagram, a selection of simplified contours (indexical), di-sound.
- the metaphor/metaform, associated with a general concept (sign of), me-sound.

Bayle, p 168. 

---

"A plunderphone is a recognizable sonic quote, using the actual sound of something familiar which has already been recorded...The plundering has to be blatant..."

Plunderphonics - Interviews

---

# Trajectories

![bg right 99%](unidirectionalTrajectory.png)

---
# Control Signals
![bg right 95%](linearSampling.png)

---

## Anchor units

Stoll, 2009.

---
## Personal Audio Corpus

---

## Application, two approaches

**_Usynlig_**, stereo fixed media (2021)

**_A More Sound Outlook &reg;_**, for marimba and bass clarinet (2021)

---

## *Usynlig*

---
![bg 55%](usynligFirstGestureBEFORE.png)

---

![bg 55%](usynligFirstGestureAFTER.png)

---
## *A More Sound Outlook &reg;*

---
![bg 55%](fft_outlookSound.png)

---
![bg](power_outlookSound.png)

---

![bg 85%](notationScreenshot.png)

---

## Future Work

---

## Analysis

---

## Mixed Music

---

## Pedagogy

---

## Interface Design