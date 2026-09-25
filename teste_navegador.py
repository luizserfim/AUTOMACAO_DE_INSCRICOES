from src.navegador import iniciar_navegador, acessar_site


driver = iniciar_navegador()

acessar_site(driver)

input("\nPressione ENTER para fechar o Firefox...")

driver.quit()
