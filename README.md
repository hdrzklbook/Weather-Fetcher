# Weather Fetcher

This Python script fetches the current weather for a given city using the free Open-Meteo API.

## Features

- Geocodes the city name to latitude/longitude using Open-Meteo's Geocoding API
- Fetches current temperature, windspeed, and weather code
- No API key required

## Usage

1. Make sure you have Python 3 and `requests` installed:
   ```bash
   pip install requests
   ```
2. Save the script as `weather_fetcher.py`.
3. Run the script:
   ```bash
   python weather_fetcher.py
   ```
4. Enter the city name when prompted.

## Example Output

```
Enter city name: Tokyo
Current weather in Tokyo:
  Temperature: 28.4°C
  Windspeed: 18.3 km/h
  Weather Code: 1
```

## Weather Code Reference

See [Open-Meteo Documentation](https://open-meteo.com/en/docs) for details on weather code meanings.

## License

This project is provided under the MIT License.
