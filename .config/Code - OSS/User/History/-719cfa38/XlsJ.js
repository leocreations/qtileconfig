import { StatusBar } from 'expo-status-bar';
import { Image, StyleSheet, Text, View, Button, TouchableHighlight } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Image source={{ uri: "https://uvejuegos.com/img/caratulas/623/Japonesa_Bajandochems.jpg" }} style={{ width:215, height:294 }} resizeMode='contain' />
      <Text style={{ color: "#fff" }}>Zelda Ocarina Of Time</Text>
      <StatusBar style="light" />
      <Button title="Pulsa aqui" onPress={() => alert("Hello world")}/>
      <TouchableHighlight
        underlayColor={"#09f"}
        onPress={() => alert("Helloo")}
        style={{ width: 200, height: 200, backgroundColor: "red", borderRadius: 1000, justifyContent: "center", alignItems: "center" }}
      />
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
