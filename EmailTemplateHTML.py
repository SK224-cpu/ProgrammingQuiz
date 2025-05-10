from bs4 import BeautifulSoup
import random
import datetime

def generate_email_html_N_plaintext(name, question_sources):
    motivational_messages = [
    f"""<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">I know learning programming can feel a little intimidating at first — that’s totally normal. Every developer you admire once felt the same way. What matters most is that you’ve started, and that’s a huge step many never take.</p>
        <p style="font-size: 16px; color: #333;">Mistakes will happen — and that’s not failure, it’s how real learning begins. Be patient with yourself, stay curious, and celebrate even the small wins.</p>
        <p style="font-size: 16px; color: #333;">You’re not alone on this journey, and you absolutely have what it takes. Just keep moving forward — one line of code at a time.</p>
        <p style="font-size: 16px; color: #333;">Proud of you already! 🚀<br>Let’s code something awesome.</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">Starting something new like programming can feel overwhelming — but every great developer began right where you are. What matters is that you’re here, learning, growing, and showing up.</p>
        <p style="font-size: 16px; color: #333;">You’re doing amazing. Keep going — one bug fix, one function at a time.</p>
        <p style="font-size: 16px; color: #333;">You've got this! 🚀</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">It’s okay to feel unsure — coding is like learning a new language, and confusion is part of the process.</p>
        <p style="font-size: 16px; color: #333;">Just remember: every error message is a step forward, not back. Trust yourself. You’re learning more than you realize.</p>
        <p style="font-size: 16px; color: #333;">Keep building — you’re on the right path!</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">You’re doing something powerful by learning to code. It's not easy — and that’s what makes it so rewarding.</p>
        <p style="font-size: 16px; color: #333;">Every small win counts, and every misstep teaches you something valuable.</p>
        <p style="font-size: 16px; color: #333;">Believe in your journey. One line of code at a time, you’re becoming a developer. 🙌</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">Don’t worry if things don’t make sense right away — that’s part of the magic of learning to program.</p>
        <p style="font-size: 16px; color: #333;">The fact that you’re even trying sets you apart. Be patient, be kind to yourself, and keep at it.</p>
        <p style="font-size: 16px; color: #333;">You’re doing better than you think.</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">Programming can seem tough — but so are you. Every developer has doubted themselves at the beginning.</p>
        <p style="font-size: 16px; color: #333;">What matters is that you don’t give up. Stay curious, break problems into small pieces, and celebrate every step.</p>
        <p style="font-size: 16px; color: #333;">You’re building something awesome — starting with yourself.</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">Every programmer starts with questions, confusion, and curiosity.</p>
        <p style="font-size: 16px; color: #333;">It’s okay to be unsure — that means you’re pushing yourself to grow.</p>
        <p style="font-size: 16px; color: #333;">Keep showing up, keep typing, and keep believing. The confidence comes with the code.</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">Think of each challenge as a puzzle, not a problem. Even the greatest coders stumble — and that’s how they become great.</p>
        <p style="font-size: 16px; color: #333;">Mistakes mean you’re trying. Progress means you’re learning.</p>
        <p style="font-size: 16px; color: #333;">Keep going — the future developer in you will thank you. 💻</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">You don’t need to know everything. You just need to start — and you already have.</p>
        <p style="font-size: 16px; color: #333;">Every time you write code, you’re leveling up your skills.</p>
        <p style="font-size: 16px; color: #333;">So take a deep breath, try again, and smile when it clicks. You’re on your way.</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">It’s normal to feel stuck sometimes — that’s what learning feels like.</p>
        <p style="font-size: 16px; color: #333;">But you’re not stuck. You’re growing, adapting, and building new ways of thinking.</p>
        <p style="font-size: 16px; color: #333;">Be proud of your effort. This is what becoming a developer looks like.</p>
    </div>""",
    """<div style="font-size: 16px; color: #333; margin-bottom: 20px;">
        <p style="font-size: 16px; color: #333;">There’s no perfect way to learn coding. There’s just your way — full of trial, error, progress, and small victories.</p>
        <p style="font-size: 16px; color: #333;">Stick with it, take breaks, ask questions, and keep experimenting.</p>
        <p style="font-size: 16px; color: #333;">You’re closer than you think. And you’re not alone in this journey.</p>
    </div>"""
]
    message = random.choice(motivational_messages)

    questions_html = ""
    for desc, idx, question in question_sources:
        questions_html += f"""
        <li style="margin-bottom: 15px;">
            <strong style="color: #2c3e50;">{desc}</strong><br>
            <span style="color: #333;">Q{idx}: {question}</span>
        </li>"""

    htmlEmailMessage = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Ready to Code? Your Programming Quiz Awaits 🚀</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
      <div style="max-width: 600px; margin: auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        
        <!-- Header Image -->
        <img src="https://i.ibb.co/p6TN9GYb/programming-quiz-header.png" alt="Programming Quiz Banner" style="width: 100%; border-radius: 8px; margin-bottom: 20px;">

        <h2 style="color: #2c3e50;">Hey {name},</h2>
        <b style="font-size: 14px; color: #777; margin-top: -10px;">{datetime.date.today}</b>  
         {message}
        <hr style="margin: 30px 0;">
        <h3 style="color: #2c3e50;">Here are your questions:</h3>
        <ol>
          {questions_html}
        </ol>
      </div>
    </body>
    </html>
"""
    soup = BeautifulSoup(htmlEmailMessage, "html.parser")
    plainEmailMessage = soup.get_text()
    return (htmlEmailMessage, plainEmailMessage)



# html = generate_email_html("Shruti", question_sources)
# print(html[0])