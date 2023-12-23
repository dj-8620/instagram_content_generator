import re
from loguru import logger


def create_instragram_prompt_from_description_list(description_list):
    """Return a prompt to generate an Instagram caption from an description list."""
    logger.info("Creating Instagram prompt from description list")
    clean_list = clean_description_list(description_list)
    prompt_intro = (
        "Using the following list of descriptions of news articles below, determine the "
        "trending technology topic. Then, use the knowledge about the articles to generate "
        "an Instagram caption for a technology consulting company Long Acre Solutions. The "
        "company slogan is 'Elevate your brand. Expand your reach.' They focus on developing "
        "business solutions for companies, from web development to enterprise-level applications, "
        "to AI solutions, to Data Science. Make the post around the trending topic in the news but "
        "also make sure to highlight how Long Acre Solutions can help your company. Create hashtags "
        "to match the post. Ensure the last two hashtags are always #LongAcreSolutions, "
        "#ElevateYourBrand, and #ExpandYourReach. Returning only the caption.\n###\n"
    )
    return prompt_intro + "\n".join(clean_list)


def remove_special_chars(text):
    """Remove newline, carriage return and tab characters from text."""
    pattern = r"[\n\r\t]"
    # Replace the matched patterns with an empty string
    return re.sub(pattern, '', text)


def clean_description_list(description_list):
    """Remove special characters from the description list."""
    return [remove_special_chars(description) for description in description_list]

