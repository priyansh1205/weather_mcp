from fastmcp import FastMCP

# Create FastMCP server instance with SSE transport
mcp = FastMCP("Weather Server 🌤️")

@mcp.tool
def get_current_weather(location: str) -> str:
    """Get current weather conditions for a location"""
    import random
    temps = [20, 25, 18, 30, 15, 22]
    conditions = ["sunny", "cloudy", "rainy", "partly cloudy", "windy"]
    return f"Current weather in {location}: {random.choice(temps)}°C, {random.choice(conditions)}"

@mcp.tool
def get_weather_forecast(location: str, days: int = 5) -> str:
    """Get weather forecast for specified number of days"""
    import random
    from datetime import datetime, timedelta
    
    forecast = []
    for i in range(min(days, 7)):
        date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        temp = random.randint(15, 30)
        condition = random.choice(["sunny", "rainy", "cloudy", "windy"])
        forecast.append(f"{date}: {temp}°C, {condition}")
    return f"Weather forecast for {location}:\n" + "\n".join(forecast)

@mcp.tool
def check_rain_probability(location: str) -> str:
    """Check probability of rain for today"""
    import random
    probability = random.randint(0, 100)
    return f"Rain probability in {location} today: {probability}%"

@mcp.tool
def get_temperature_alerts(location: str) -> str:
    """Get temperature alerts and warnings"""
    import random
    alerts = ["Heat wave warning", "Cold weather advisory", "Normal temperatures", "Extreme heat alert"]
    return f"Temperature alert for {location}: {random.choice(alerts)}"

@mcp.tool
def get_weather_summary(location: str) -> str:
    """Get comprehensive weather summary"""
    import random
    temp = random.randint(15, 30)
    humidity = random.randint(40, 80)
    wind = random.randint(5, 25)
    return f"Weather summary for {location}: {temp}°C, {humidity}% humidity, {wind} km/h wind"

if __name__ == "__main__":
    # Run with SSE transport for internet access
    mcp.run(transport="sse", host="0.0.0.0", port=8001)
