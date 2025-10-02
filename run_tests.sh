#!/bin/bash

# 1. Ejecutar las pruebas y generar los archivos intermedios de Allure
echo "Ejecutando pruebas con Behave y generando resultados de Allure..."
behave features/login.feature -f allure_behave.formatter:AllureFormatter -o allure-results

# Verificar si behave falló
if [ $? -ne 0 ]; then
    echo "Las pruebas fallaron. Generando reporte parcial..."
fi

# 2. Generar el reporte HTML final (sobrescribiendo el anterior)
echo "Generando reporte Allure final..."
allure generate allure-results --clean -o allure-report

# 3. Abrir el reporte en el navegador
echo "Abriendo reporte en el navegador..."
allure open allure-report