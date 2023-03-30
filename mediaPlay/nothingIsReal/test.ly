\version "2.24.1"
\language "english"

\include "/Users/hse9/Library/Application Support/SCAMP/scamp_lilypond_template.ly"
\header
{
    title = \markup { Code To Joy }
    composer = \markup { PHPrince }
}
\score
{
    \new Score
    <<
        \context Staff = "goblin"
        \with
        {
            instrumentName = #"goblin"
        }
        {
            <<
                \context Voice = "voiceOne"
                {
                    \time 4/4
                    \clef "treble"
                    g''4
                    d'''8
                    b''8
                    b''4
                    a''8
                    g''8
                    ~
                }
                \context Voice = "TempoVoice"
                {
                    \tempo 4=60
                    s1
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    g''4.
                    g'8
                    c''8
                    c''8
                    b'8
                    a'8
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    a'8
                    g'4.
                    ~
                    g'8
                    g'8
                    d''8
                    b'8
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    b'8
                    a'8
                    a'8
                    g'8
                    g'8
                    e'4.
                    ~
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    e'4.
                    d'8
                    ~
                    d'8
                    b4
                    a8
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    \clef "bass"
                    g4
                    b8
                    b8
                    c'8
                    b4
                    a8
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    g8
                    f8
                    e8
                    d8
                    ~
                    d4.
                    b,,8
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    g,,4
                    g,,16
                    e,,16
                    g,,8
                    g,,4
                    g,16
                    e,16
                    g,8
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    g,4
                    g,4
                    ~
                    g,8
                    b,4.
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    \clef "treble"
                    g''8.
                    c'''16
                    g''8
                    g''8
                    g''16
                    g''16
                    g''16
                    g''16
                    g''8
                    g''8
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    g''8.
                    g''16
                    b'''16
                    d''''8
                    b'''16
                    e''''8
                    b'''16
                    d''''16
                    ~
                    d''''16
                    d''''16
                    b'''8
                    ~
                }
            >>
            <<
                \context Voice = "voiceOne"
                {
                    b'''4.
                    r8
                    r2
                    \bar "|."
                }
            >>
        }
    >>
}