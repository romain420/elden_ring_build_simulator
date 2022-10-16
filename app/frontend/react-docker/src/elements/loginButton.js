import { StyleSheet, Button, View, SafeAreaView,Text, Alert } from 'react-native';
import '../App.css';

export function LoginButton(){
    return(
        <Button
            title="Login"
            onPress={() => Alert.alert(
            'You are going to login')}
        />
    )
}

