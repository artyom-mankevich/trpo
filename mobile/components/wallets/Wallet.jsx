import {View, StyleSheet, Text, TouchableOpacity, Alert} from "react-native";
import {Feather, FontAwesome} from "@expo/vector-icons";
import {ReduceFriendlyNumbers} from "./WalletValidation";
import getSymbolFromCurrency from "currency-symbol-map";
import {useEffect, useState} from "react";
import {format} from "date-fns";
import AsyncStorage from "@react-native-async-storage/async-storage";

export default function Wallet(props) {
    const [enabled, setEnabled] = useState(false);
    const [dateFormat, setDateFormat] = useState('d MMMM y');
    const [currencyFormat, setCurrencyFormat] = useState('left');

    const getDateFormat = async () => {
        const dateFormat = await AsyncStorage.getItem('dateFormat');
        setDateFormat(dateFormat);
        const currencFormat = await AsyncStorage.getItem('currencyFormat');
        setCurrencyFormat(currencFormat);
    }

    useEffect(() => {
        getDateFormat().then();
    },[]);

    return (
        <View style={{marginTop:10, width:350, height:250, borderRadius:30, backgroundColor:props.color}}>
            <View style={styles.walletHeader}>
            <View style={styles.walletName}>
                <Text style={styles.walletNameText} numberOfLines={3} >{props.name}</Text>
            </View>
            <View style={styles.walletBalanceInfo}>
                <View style={styles.walletBalance}>
                    {
                        currencyFormat === 'left' ? <>
                            <Text style={styles.walletBalanceText}>{getSymbolFromCurrency(props.currency)}</Text>
                            <Text style={styles.walletBalanceText}>{ReduceFriendlyNumbers(props.balance, 1)}</Text>
                        </> : <>
                            <Text style={styles.walletBalanceText}>{ReduceFriendlyNumbers(props.balance, 1)}</Text>
                            <Text style={styles.walletBalanceText}>{getSymbolFromCurrency(props.currency)}</Text>
                        </>
                    }
                </View>
                <View style={styles.walletGoal}>
                    {
                        currencyFormat === 'left' ? <>
                            <Text style={styles.walletGoalText}>{getSymbolFromCurrency(props.currency)}</Text>
                            <Text style={styles.walletGoalText}>{ReduceFriendlyNumbers(props.goal, 1)}</Text>
                        </> : <>
                            <Text style={styles.walletGoalText}>{ReduceFriendlyNumbers(props.goal, 1)}</Text>
                            <Text style={styles.walletGoalText}>{getSymbolFromCurrency(props.currency)}</Text>
                        </>
                    }
                </View>
            </View>
                </View>
            <View style={styles.walletFooter}>
                    <View style={styles.walletUpdateInfo}>
                        <Text style={styles.walletUpdateText}>Last Update:</Text>
                        <Text style={styles.walletUpdateText}>
                            {
                                format(new Date(props.lastUpdated), dateFormat)
                            }
                        </Text>
                    </View>
                    <View style={styles.walletUpdateBtn}>
                        {
                            !props.createElement &&
                            <View>
                            {enabled &&
                            <View style={styles.walletDeleteBtn}>
                                <TouchableOpacity
                                    style={styles.walletDeleteBtnTouchableOpacity}
                                    onPress={() => props.onDeleted()}>
                                    <FontAwesome name="trash" size={55} color="#930000"/>
                                </TouchableOpacity>
                            </View>
                        }
                            </View>
                        }
                        <TouchableOpacity
                            style={styles.walletUpdateBtnTouchableOpacity}
                            onPress={() => {
                                props.createElement ? setEnabled(false) : setEnabled(!enabled);

                            }}
                            key={props.name}
                        >
                            <View style={styles.walletUpdateCircle}>
                                <Feather name="circle" size={60} color={enabled ? '#D7D7D7E5' : '#fff'} />
                            </View>
                            <View style={styles.walletUpdateGear}>
                                <FontAwesome name="gear" size={37} color={enabled ? '#D7D7D7E5' : '#fff'} />
                            </View>
                        </TouchableOpacity>
                    </View>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    wallet: {
        width: 350,
        height: 250,
        backgroundColor: '#3e68d1',
        borderRadius: 30,
    },
    walletHeader: {
        flexDirection: 'row',
    },
    walletName: {
        textAlign: 'left',
        paddingLeft: 30,
        paddingTop: 20,
        width: 170,
        height: 140,
    },
    walletNameText: {
        color: '#fff',
        fontSize: 30,
        fontWeight: '700',
    },
    walletBalanceInfo: {
        flexDirection: 'column',
        marginLeft: 'auto',
        paddingTop: 20,
        paddingRight: 10,
    },
    walletBalance: {
        flexDirection: 'row',
        marginLeft: 'auto',
    },
    walletBalanceText: {
        color: '#fff',
        fontSize: 30,
        fontWeight: '700',
        paddingRight: 5,
    },
    walletGoal: {
        flexDirection: 'row',
        marginLeft: 'auto',
    },
    walletGoalText: {
        color: '#fff',
        fontSize: 20,
        fontWeight: '400',
        paddingRight: 5,
    },
    walletFooter: {
        flexDirection: 'row',
        bottom: 40,
    },
    walletUpdateInfo: {
        flexDirection: 'column',
        paddingLeft: 30,
        top: 70,
    },
    walletUpdateText: {
        color: '#fff',
        fontSize: 16,
    },
    walletUpdateBtn: {
        flexDirection: 'row',
        marginLeft: 'auto',
        top: 65,
    },
    walletUpdateBtnTouchableOpacity: {
        width: 100,
        height: 100,
        justifyContent: 'center',
        alignItems: 'center',
    },
    walletUpdateGear: {
        bottom: 50,
    },
    walletDeleteBtn: {
        position: 'absolute',
        bottom: 110,
        left: 29,
    },
});