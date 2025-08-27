import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_admin_dashboard_ui():
    """Test the UI elements of the custom admin dashboard."""
    # Initialize the WebDriver (Chrome in this case)
    driver = webdriver.Chrome()
    
    try:
        # Navigate to the login page
        driver.get('http://localhost:8000/custom-admin/login/')
        
        # Login as staff user
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        
        username_input.send_keys('staffuser')  # Replace with your staff username
        password_input.send_keys('testpassword')  # Replace with your staff password
        submit_button.click()
        
        # Wait for dashboard to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.stat-card'))
        )
        
        # Test dashboard UI elements
        print("Testing dashboard UI elements...")
        
        # Check stat cards
        stat_cards = driver.find_elements(By.CSS_SELECTOR, '.stat-card')
        print(f"Found {len(stat_cards)} stat cards")
        assert len(stat_cards) == 4, "Expected 4 stat cards"
        
        # Check financial summary
        financial_summary = driver.find_element(By.CSS_SELECTOR, '.card-title')
        assert "Financial Summary" in financial_summary.text, "Financial Summary not found"
        
        # Check transaction chart
        transaction_chart = driver.find_element(By.ID, 'transactionChart')
        assert transaction_chart.is_displayed(), "Transaction chart not displayed"
        
        # Test chart/table toggle
        toggle_button = driver.find_element(By.CSS_SELECTOR, '.chart-toggle-btn')
        toggle_button.click()
        time.sleep(1)  # Wait for toggle animation
        
        # Check if table is now visible
        transaction_table = driver.find_element(By.CSS_SELECTOR, '.transaction-stats-table')
        assert transaction_table.is_displayed(), "Transaction table not displayed after toggle"
        
        # Test transaction filters
        filter_dropdown = driver.find_element(By.ID, 'transactionFilterDropdown')
        filter_dropdown.click()
        time.sleep(1)  # Wait for dropdown to open
        
        # Click on Sales Only filter
        sales_filter = driver.find_element(By.CSS_SELECTOR, '.dropdown-item[data-filter="sale"]')
        sales_filter.click()
        time.sleep(1)  # Wait for filtering to apply
        
        # Test refresh button
        refresh_button = driver.find_element(By.CSS_SELECTOR, '.btn-refresh')
        refresh_button.click()
        time.sleep(1)  # Wait for spin animation
        
        # Test sidebar toggle
        sidebar_toggle = driver.find_element(By.ID, 'toggle-sidebar')
        sidebar_toggle.click()
        time.sleep(1)  # Wait for sidebar animation
        
        # Check if sidebar is collapsed
        body = driver.find_element(By.TAG_NAME, 'body')
        assert 'sidebar-collapsed' in body.get_attribute('class'), "Sidebar not collapsed"
        
        print("All UI tests passed!")
        
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_admin_dashboard_ui()