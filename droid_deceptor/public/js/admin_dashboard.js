  function changeTab(tabName) {
    // Get all tabs and sections
    const tabs = document.querySelectorAll('.tabs a');
    const sections = document.querySelectorAll('.transfer-section, .payment-section, .service-section');

    // Remove 'active' class from all tabs and sections
    tabs.forEach(tab => tab.classList.remove('active'));
    sections.forEach(section => section.classList.remove('active'));

    // Add 'active' class to the clicked tab and corresponding section
    const selectedTab = document.querySelector(`.tabs a[onclick="changeTab('${tabName}')"]`);
    const selectedSection = document.getElementById(tabName);

    if (selectedTab && selectedSection) {
      selectedTab.classList.add('active');
      selectedSection.classList.add('active');
    }
  }
