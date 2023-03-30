\version "2.24.1"
\language "english"

\paper {
  #(set-paper-size "letter")
  ragged-last-bottom = ##t
  ragged-bottom = ##f
}
\header
{
    title = "Nothing is Real"
    subtitle = "(Allstar)"
    composer = \markup { Alvin Lucier/Smash Mouth/MediaPlay }
    tagline = ##f
}
\markup \vspace #3
#(set-global-staff-size 22)
\score
{
    \new Score
    <<
        \context Staff = "pno."
        \with
        {
            instrumentName = #"pno"
        }
        {
            <<
                \context Voice = "voiceOne"
                {
                    \time 4/4
                    \clef "treble"
		    \ottava #1
  		    \set Staff.ottavation = #"8va"
		    \set Staff.explicitClefVisibility = #end-of-line-invisible
		    \omit Score.BarLine
                    g''4 \noBreak
                    d'''8 \noBreak
                    b''8  \noBreak
                    b''4  \noBreak
                    a''8  \noBreak
                    g'' 1
		    \ottava #0
		    \break
                    g'8  \noBreak
                    c''4 \noBreak
                    b'8  \noBreak
                    b'8  \noBreak
                    a'8 \noBreak
                    a'8  \noBreak
                    g'1 \break
                    g'8  \noBreak
                    d''8 \noBreak
                    b'8  \noBreak
                    b'8  \noBreak
                    a'8  \noBreak
                    a'8  \noBreak
                    g'8  \noBreak
                    g'8  \noBreak
                    e'1 \break
                    \clef "bass"
                    d'4 \noBreak
                    b4  \noBreak
                    a8 \noBreak
                    g4  \noBreak
                    b4  \noBreak
                    c'8 \noBreak
                    b4  \noBreak
                    a8 \noBreak
                    g8  \noBreak
                    e8  \noBreak
                    d1 \break
		    \ottava #1
  		    \set Staff.ottavation = #"32vb"
                    b8 \noBreak
                    g4  \noBreak
                    g16 \noBreak
                    e16 \noBreak
                    g8  \noBreak
                    g1  \break
		    \ottava #0
		    \ottava #1
		    \set Staff.ottavation = #"16vb"
                    g16  \noBreak
                    e16  \noBreak
                    g8 \noBreak
                    g4  \noBreak
                    g4.  \noBreak
                    b1 \break
		    \ottava #0
		    \ottava #1
		    \set Staff.ottavation = #"8va"
                    \clef "treble"
                    g''8.  \noBreak
                    d'''16 \noBreak
                    g''8   \noBreak
                    g''8   \noBreak
                    g''16  \noBreak
                    g''16  \noBreak
                    g''16  \noBreak
                    g''16  \noBreak
                    g''8   \noBreak
                    g'8 \noBreak
                    g''1  \break
                    \ottava #0
		    \ottava #1
		    \set Staff.ottavation = #"16va"
                    b''16 \noBreak
                    d'''8 \noBreak
                    b''16 \noBreak
                    e'''8 \noBreak
                    b''16 \noBreak
                    d'''8 \noBreak
                    d'''16 \noBreak
                    b''1
		    \ottava #0
                }
            >>
        }
    >>
}
