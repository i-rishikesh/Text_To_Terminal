import streamlit as st

@st.cache
def get_data():
  return pd.read_csv('data.csv')

def main():
  data = get_data()

  # Add a CLI to your app
  parser = argparse.ArgumentParser()
  parser.add_argument('--name', type=str, default='John Doe')
  args = parser.parse_args()

  # Display the data
  st.write(data)

  # Display the name
  st.write(f'Hello, {args.name}!')

if __name__ == '__main__':
  main()