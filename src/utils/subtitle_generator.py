import asyncio

async def generate_subtitles():
    await asyncio.sleep(5)  # Simulate processing time
    return {
        'srt': """1
00:00:01,000 --> 00:00:04,000
Hello, welcome to our multi-subtitle generator.

2
00:00:04,500 --> 00:00:08,000
This is a sample SRT file content.""",

        'vtt': """WEBVTT

00:00:01.000 --> 00:00:04.000
Hello, welcome to our multi-subtitle generator.

00:00:04.500 --> 00:00:08.000
This is a sample VTT file content.""",

        'txt': """Hello, welcome to our multi-subtitle generator.
This is a sample TXT file content."""
    }