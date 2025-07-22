# Twitter Bot with GUI

> ⚠️ **API Limitation Warning**: This bot requires a paid Twitter API subscription (minimum Basic tier - $100/month) to function properly. Free API access will not work with most features. See [Service Limitations](#service-limitations) section for details.

A Python-based Twitter bot with a graphical user interface that allows you to automate various Twitter interactions such as searching, liking, retweeting, and replying to tweets.

## Features

- Search for tweets using keywords
- Like tweets automatically
- Retweet posts automatically
- Reply to tweets with custom messages
- Follow users automatically
- User-friendly GUI interface
- Secure credential management using environment variables

## Prerequisites

- Python 3.8 or higher
- Twitter Developer Account with API access
- Twitter API credentials (API key, API secret, Access token, Access token secret)

## Installation

1. Clone the repository:
2. Install required dependencies:
3. Create a `.env` file in the project root directory with your Twitter API credentials:
   TWITTER_CONSUMER_KEY=your_api_key
   TWITTER_CONSUMER_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret


## Usage

1. Run the bot:
2. The GUI will appear with the following input fields:
   - Search: Enter keywords to search for tweets
   - Number of Tweets: Specify how many tweets to process
   - Response: Enter the message you want to reply with
   - Reply (yes/no): Choose whether to reply to tweets
   - Favorite (yes/no): Choose whether to like tweets
   - Retweet (yes/no): Choose whether to retweet
   - Follow (yes/no): Choose whether to follow users

3. Click the "Submit" button to start the bot

## Configuration

The bot uses the following environment variables:
- `TWITTER_CONSUMER_KEY`: Your Twitter API key
- `TWITTER_CONSUMER_SECRET`: Your Twitter API secret
- `TWITTER_ACCESS_TOKEN`: Your Twitter access token
- `TWITTER_ACCESS_TOKEN_SECRET`: Your Twitter access token secret

## Dependencies

- tweepy: Twitter API wrapper for Python
- python-dotenv: Environment variable management
- tkinter: GUI library (included with Python)

## Important Notes

- Make sure to comply with Twitter's API usage guidelines and rate limits
- Keep your API credentials secure and never share them
- The bot requires Twitter API v2 access
- Some features may be limited based on your API access level

## Error Handling

The bot includes error handling for:
- Authentication errors
- API rate limits
- Invalid input values
- Network issues
- Twitter API exceptions

## ⚠️ Service Limitations

**Important Notice**: As of February 2024, Twitter (X) has significantly changed its API access policy:

1. **Basic (Free) API Access**:
   - Limited to read-only operations
   - No access to search functionality
   - Restricted tweet posting capabilities
   - Rate limited to 1,500 tweets per month

2. **Basic Tier ($100/month)**:
   - Required for most bot functionalities
   - Includes search API access
   - Allows posting tweets
   - Up to 10,000 tweets per month
   - Access to like, retweet, and reply features

3. **Pro Tier ($5000/month)**:
   - Full API access
   - Higher rate limits
   - Advanced features

**Impact on This Bot**: 
Due to these restrictions, this bot will not function properly with a free API key. To use this bot's full functionality, you will need at least a Basic tier subscription from Twitter's API platform. Without a paid subscription, you will encounter "403 Forbidden" errors when attempting to use features like search, automated replies, or bulk interactions.

**Alternatives**:
- Consider using the bot with reduced functionality (reading timeline only)
- Use Twitter's official tools for basic interactions
- Explore other social media platforms with more accessible APIs

For more information about Twitter's API pricing and limitations, visit their [Developer Portal](https://developer.twitter.com/en/portal/pricing).

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is for educational purposes only. Make sure to follow Twitter's terms of service and API usage guidelines when using this bot.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Acknowledgments

- Twitter API Documentation
- Tweepy Documentation
- Python tkinter Documentation

## More links
https://www.freecodecamp.org/news/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607
