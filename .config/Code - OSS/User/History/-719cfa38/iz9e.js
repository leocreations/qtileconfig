import { StatusBar } from 'expo-status-bar';
import { Image, StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Image source={{ uri: "https://uvejuegos.com/img/caratulas/623/Japonesa_Bajandochems.jpg" }} style={{ width:100, height:250 }} resizeMode='contain' />
      <Text style={{ color: "#fff" }}>Main title</Text>
      <StatusBar style="light" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
