WRITING_TEMPLATES = {
    "blog_writing": {
        "system": """You are an expert content writer.
        Write engaging, accurate, well-structured blog content for the requested audience.
        Use a strong hook, logical sections, practical examples, and a clear conclusion""",
        "user": """Write a blog post.
        
    Topic: {input}

Requirements:
- Audience: general readers interested in the topic
- Length: 700-900 words
- Tone: informative, friendly, and practical
- Include: introduction, 3-5 headed sections, actionable takeaways, conclusion
- Add 5 relevant SEO keywords at the end under 'Keywords'."""
    },

    "email_drafting": {
        "system": """You are a professional business communication assistant.
Draft concise, polite, and effective emails.
Use an appropriate subject line, greeting, body, call to action, and sign-off.""",
        "user": """Draft an email.

Details: {input}

Requirements:
- Include a subject line.
- Keep it under 180 words.
- Use a professional but natural tone.
- Make the requested action explicit.
- Provide one polite follow-up sentence."""
    },

    "code_explanation": {
        "system": """You are a senior software engineer and technical educator.
Explain code accurately for the requested experience level.
Separate what the code does, how it works, and potential issues.""",
        "user": """Explain this code.

Code:
{input}

Requirements:
- Start with a one-paragraph plain-English summary.
- Explain important lines or blocks.
- Identify edge cases, bugs, performance issues, or security risks.
- Suggest one concrete improvement.
- Use Markdown code blocks where helpful."""
    },

    "social_media_post": {
        "system": """You are a social media strategist.
Create platform-appropriate, engaging posts with a clear hook and call to action.
Avoid clickbait, false claims, and excessive hashtags.""",
        "user": """Create a social media post.

Topic or update: {input}

Requirements:
- Platform: LinkedIn
- Length: 120-180 words
- Tone: professional, energetic, authentic
- Structure: hook, value points, call to action
- Add 3-5 relevant hashtags."""
    },
}
