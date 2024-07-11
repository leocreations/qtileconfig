import { StatusBar } from 'expo-status-bar';
import { Image, StyleSheet, Text, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={{ color: "#fff" }}>Main title</Text>
      <Image source={{ uri: "https://uvejuegos.com/img/caratulas/623/Japonesa_Bajandochems.jpg" }} style={{ width:25, height:25 }} />
      <StatusBar style="dark" />
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
