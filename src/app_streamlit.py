# src/mnist_gan_app/app_streamlit.py

import streamlit as st

from src.generator_service import DigitGeneratorService


def main() -> None:
    st.set_page_config(
        page_title="Generador de dígitos manuscritos (DCGAN + MNIST)",
        page_icon="🧠",
        layout="centered",
    )

    st.title("🧠 Generador de dígitos manuscritos")
    st.write(
        """
        Esta es una aplicación de ejemplo que utiliza una **DCGAN** entrenada sobre el
        dataset **MNIST** para generar dígitos manuscritos (0–9).

        Sirve como referencia sencilla para la Evidencia de Aprendizaje 3:
        - Carga de modelo generativo.
        - Generación de nuevos ejemplos.
        - Interfaz web con Streamlit.
        """
    )

    # Inicializar el servicio (se guarda en el estado de sesión para no recargarlo siempre)
    if "digit_service" not in st.session_state:
        try:
            st.session_state["digit_service"] = DigitGeneratorService()
        except FileNotFoundError as e:
            st.error(str(e))
            st.stop()

    service: DigitGeneratorService = st.session_state["digit_service"]

    st.sidebar.header("⚙️ Parámetros de generación")
    num_images = st.sidebar.slider(
        "Número de dígitos a generar",
        min_value=4,
        max_value=64,
        value=16,
        step=4,
        help="Cantidad de imágenes que se mostrarán en la cuadrícula.",
    )

    st.sidebar.info(
        "💡 Tip: cambia el número de imágenes y vuelve a generar para ver más ejemplos."
    )

    if st.button("✨ Generar nuevos dígitos"):
        grid_np = service.generate_grid(num_images=num_images)
        st.image(grid_np, caption="Dígitos generados por la DCGAN", use_column_width=True)
    else:
        st.write("Haz clic en **'✨ Generar nuevos dígitos'** para ver muestras generadas.")

    st.markdown("---")
    st.caption(
        "Ejemplo académico para IA Generativa (DCGAN + MNIST). "
        "Puedes usar este proyecto como referencia para tu propia EA3."
    )


if __name__ == "__main__":
    main()
