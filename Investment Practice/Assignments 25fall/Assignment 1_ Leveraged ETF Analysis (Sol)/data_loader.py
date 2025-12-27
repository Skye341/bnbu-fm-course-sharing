#!/usr/bin/env python3
"""
Data Loading Module for Leveraged ETF Assignment
This module provides pre-downloaded QQQ and TQQQ data for student analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_etf_data():
    """
    Load pre-downloaded QQQ and TQQQ price and return data

    Returns:
    --------
    prices : pd.DataFrame
        Daily adjusted close prices for QQQ and TQQQ
    returns : pd.DataFrame
        Daily returns for QQQ and TQQQ
    """
    try:
        # Load price data
        prices = pd.read_csv('qqq_tqqq_prices.csv', index_col=0, parse_dates=True)

        # Load returns data
        returns = pd.read_csv('qqq_tqqq_returns.csv', index_col=0, parse_dates=True)

        # Clean any missing data
        prices = prices.dropna()
        returns = returns.dropna()

        return prices, returns

    except FileNotFoundError as e:
        print(f"❌ Error: Data file not found - {e}")
        print("📁 Make sure you have the following files in your working directory:")
        print("   • qqq_tqqq_prices.csv")
        print("   • qqq_tqqq_returns.csv")
        return None, None

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None, None

def get_data_summary(prices, returns):
    """
    Print summary statistics of the loaded data

    Parameters:
    -----------
    prices : pd.DataFrame
        Price data
    returns : pd.DataFrame
        Return data
    """
    if prices is None or returns is None:
        print("❌ No data to summarize")
        return

    print("📊 ETF DATA SUMMARY")
    print("=" * 50)
    print(f"📅 Date range: {prices.index[0].date()} to {prices.index[-1].date()}")
    print(f"📈 Number of observations: {len(prices)}")
    print(f"🗓️  Trading days covered: {len(prices)} days")
    print()

    print("💰 PRICE STATISTICS:")
    print(f"   QQQ price range: ${prices['QQQ'].min():.2f} - ${prices['QQQ'].max():.2f}")
    print(f"   TQQQ price range: ${prices['TQQQ'].min():.2f} - ${prices['TQQQ'].max():.2f}")
    print()

    print("📊 RETURN STATISTICS:")
    qqq_annual_return = returns['QQQ'].mean() * 252
    tqqq_annual_return = returns['TQQQ'].mean() * 252
    qqq_annual_vol = returns['QQQ'].std() * np.sqrt(252)
    tqqq_annual_vol = returns['TQQQ'].std() * np.sqrt(252)

    print(f"   QQQ:")
    print(f"     Average daily return: {returns['QQQ'].mean():.4f} ({qqq_annual_return:.2%} annualized)")
    print(f"     Daily volatility: {returns['QQQ'].std():.4f} ({qqq_annual_vol:.2%} annualized)")
    print()
    print(f"   TQQQ:")
    print(f"     Average daily return: {returns['TQQQ'].mean():.4f} ({tqqq_annual_return:.2%} annualized)")
    print(f"     Daily volatility: {returns['TQQQ'].std():.4f} ({tqqq_annual_vol:.2%} annualized)")
    print()

    # Calculate leverage ratio
    if returns['QQQ'].mean() != 0:
        leverage_ratio = returns['TQQQ'].mean() / returns['QQQ'].mean()
        print(f"🔢 Actual leverage ratio: {leverage_ratio:.2f}x (vs 3x target)")

    # Calculate correlation
    correlation = returns['QQQ'].corr(returns['TQQQ'])
    print(f"🔗 QQQ-TQQQ correlation: {correlation:.3f}")

    print("=" * 50)

def calculate_rolling_metrics(returns, window=30):
    """
    Calculate rolling volatility and correlation metrics

    Parameters:
    -----------
    returns : pd.DataFrame
        Daily returns data
    window : int
        Rolling window size in days (default: 30)

    Returns:
    --------
    pd.DataFrame with rolling metrics
    """
    if returns is None:
        print("❌ No returns data provided")
        return None

    rolling_metrics = pd.DataFrame(index=returns.index)

    # Rolling volatility (annualized)
    rolling_metrics['QQQ_volatility'] = returns['QQQ'].rolling(window=window).std() * np.sqrt(252)
    rolling_metrics['TQQQ_volatility'] = returns['TQQQ'].rolling(window=window).std() * np.sqrt(252)

    # Rolling correlation
    rolling_metrics['correlation'] = returns['QQQ'].rolling(window=window).corr(returns['TQQQ'])

    # Rolling mean returns
    rolling_metrics['QQQ_mean'] = returns['QQQ'].rolling(window=window).mean()
    rolling_metrics['TQQQ_mean'] = returns['TQQQ'].rolling(window=window).mean()

    # Rolling variance
    rolling_metrics['QQQ_variance'] = returns['QQQ'].rolling(window=window).var()
    rolling_metrics['TQQQ_variance'] = returns['TQQQ'].rolling(window=window).var()

    # Rolling leverage ratio
    rolling_metrics['leverage_ratio'] = rolling_metrics['TQQQ_mean'] / rolling_metrics['QQQ_mean']
    rolling_metrics['leverage_ratio'] = rolling_metrics['leverage_ratio'].replace([np.inf, -np.inf], np.nan)

    return rolling_metrics.dropna()

# Example usage and testing
if __name__ == "__main__":
    print("🧪 Testing data loader...")

    # Load data
    prices, returns = load_etf_data()

    if prices is not None and returns is not None:
        # Show summary
        get_data_summary(prices, returns)

        # Calculate rolling metrics
        print("\n📊 Calculating rolling metrics...")
        rolling_metrics = calculate_rolling_metrics(returns)

        if rolling_metrics is not None:
            print(f"✅ Rolling metrics calculated for {len(rolling_metrics)} observations")
            print(f"📈 Average 30-day QQQ volatility: {rolling_metrics['QQQ_volatility'].mean():.2%}")
            print(f"📈 Average 30-day correlation: {rolling_metrics['correlation'].mean():.3f}")

    print("\n🎯 Data loader ready for assignment!")